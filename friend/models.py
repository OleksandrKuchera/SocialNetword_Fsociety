from django.db import models
from account.models import CustomUser

class Friend(models.Model):
    user = models.ForeignKey(CustomUser, related_name='friends', on_delete=models.CASCADE)
    friend = models.ForeignKey(CustomUser, related_name='user_friends', on_delete=models.CASCADE)
    isFollow = models.BooleanField(default=False)  

    class Meta:
        unique_together = ('user', 'friend')

        