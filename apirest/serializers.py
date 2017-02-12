from apirest.models import Comment
from rest_framework import serializers


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'owner', 'body', 'marker', 'karma', 'date')