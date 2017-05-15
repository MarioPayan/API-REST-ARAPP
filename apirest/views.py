from apirest.models import Comment, User, Vote
from rest_framework import viewsets
from apirest.serializers import CommentSerializerCreate, CommentSerializerDetail, UserSerializerDetail, UserSerializerCreate
from rest_framework.decorators import list_route, detail_route
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializerCreate
    queryset = Comment.objects.all()
        
    @detail_route()
    def upvote(self, request, pk):
        comment = Comment.objects.get(id=pk)
        owner = request.user
        if(not Vote.objects.filter(owner=owner, comment=comment).exists() or Vote.objects.get(owner=owner, comment=comment).state==-1):
            vote, created = Vote.objects.update_or_create(owner=owner, comment=comment, defaults={"state":1})
            add = 1 if created else 2
            comment.karma = comment.karma + add
            comment.save()
            
            return Response({"status": "upvoted"})
        else:
            return Response({"status": "not upvoted"})
        
    @detail_route()
    def downvote(self, request, pk):
        comment = Comment.objects.get(id=pk)
        owner = request.user
        if(not Vote.objects.filter(owner=owner, comment=comment).exists() or Vote.objects.get(owner=owner, comment=comment).state==1):
            vote, created = Vote.objects.update_or_create(owner=owner, comment=comment, defaults={"state":-1})
            add = 1 if created else 2
            comment.karma = comment.karma - add
            comment.save()
            
            return Response({"status": "downvoted"})
        else:
            return Response({"status": "not downvoted"})

    @detail_route()
    def clearvote(self, request, pk):
        comment = Comment.objects.get(id=pk)
        owner = request.user
        if(Vote.objects.filter(owner=owner, comment=comment).exists()):
            state = Vote.objects.get(owner=owner, comment=comment).state
            Vote.objects.get(owner=owner, comment=comment).delete()
            add = 1 if (state==-1) else -1 if (state==1) else 0
            comment.karma = comment.karma + add
            comment.save()
            return Response({"status": "clearvoted"})
        
        else:
            return Response({"status": "not clearvoted"})


class CommentByMarkerView(generics.ListAPIView):
    serializer_class = CommentSerializerDetail

    def get_queryset(self):
        marker = self.kwargs['marker']
        return Comment.objects.filter(marker=marker)
        

class CommentByMarkerViewOrderKarma(generics.ListAPIView):
    serializer_class = CommentSerializerDetail

    def get_queryset(self):
        marker = self.kwargs['marker']
        return Comment.objects.filter(marker=marker).order_by('-karma')
        

class CommentByMarkerViewOrderDate(generics.ListAPIView):
    serializer_class = CommentSerializerDetail

    def get_queryset(self):
        marker = self.kwargs['marker']
        return Comment.objects.filter(marker=marker).order_by('-date')


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializerDetail
    queryset = User.objects.all()
    
    @list_route(methods=['get'], url_path='(?P<username>\w+)')
    def getByUsername(self, request, username ):
        user = get_object_or_404(User, username=username)
        return Response(UserSerializerDetail(user).data)
    
    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return UserSerializerCreate
        else:
            return UserSerializerDetail