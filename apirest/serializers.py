from apirest.models import Comment, User, Vote
from rest_framework import serializers


class CommentSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'owner', 'body', 'marker', 'date')

class CommentSerializerDetail(serializers.ModelSerializer):
    voted = serializers.SerializerMethodField('is_voted')

    def is_voted(self, obj):
        user = self.context['request'].user.id
        vote = Vote.objects.filter(owner=user, comment=obj.id)
        if vote.exists():
            return vote[0].state
        else:
            return 0
            
    class Meta:
        model = Comment
        fields = ('id', 'owner', 'body', 'marker', 'karma', 'date', 'voted')


class CommentSerializerKarma(serializers.ModelSerializer):
    voted = serializers.SerializerMethodField('is_voted')

    def is_voted(self, obj):
        user = self.context['request'].user.id
        vote = Vote.objects.filter(owner=user, comment=obj.id)
        if vote.exists():
            return vote[0].state
        else:
            return 0
            
    class Meta:
        model = Comment
        fields = ('id', 'owner', 'body', 'marker', 'karma', 'date', 'voted')


class UserSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
    
    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

        
class UserSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class VoteSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('__all__')