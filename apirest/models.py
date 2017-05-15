from django.db import models
from django.contrib.auth.models import User

    
class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    body = models.CharField(max_length=180)
    marker = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    karma = models.IntegerField(default=0)
    current_user = 0

    def set_user(self, user_id):
        self.current_user = user_id


class Vote(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=False)
    type_votes = (
            (1, 'upvote'),
            (-1, 'downvote'),
            (0, 'unvote')
        )
    state = models.IntegerField(choices=type_votes, default=0)