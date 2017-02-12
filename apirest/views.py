from apirest.models import Comment
from rest_framework import viewsets
from apirest.serializers import CommentSerializer
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from rest_framework import generics


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    
    @detail_route()
    def upvote(self, request, pk):
        comment = Comment.objects.get(id=pk)
        comment.karma = comment.karma + 1
        comment.save()
        return Response({"status": "upvoted"})
        

class CommentByMarkerView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        marker = self.kwargs['marker']
        return Comment.objects.filter(marker=marker)
        

class CommentByMarkerViewOrderKarma(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        marker = self.kwargs['marker']
        return Comment.objects.filter(marker=marker).order_by('-karma')
        

class CommentByMarkerViewOrderDate(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        marker = self.kwargs['marker']
        return Comment.objects.filter(marker=marker).order_by('-date')

