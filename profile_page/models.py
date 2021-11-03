from django.db import models
from django.utils import timezone

class Profile(models.Model):
    profile_name = models.CharField(max_length=20)
    id = models.BigAutoField(primary_key=True)
    creation_date = models.DateField(default=timezone.now)
    profile_hashtag = models.CharField(max_length=20)
    followers = models.IntegerField()
    following = models.IntegerField()
    tweet_content = models.CharField(max_length=200)
    tweet_number = models.IntegerField()

    def __str__(self):
        return self.profile_name



class Tweet(models.Model):
    id = models.BigAutoField(primary_key=True)
    creation_date = models.DateField(default=timezone.now)
    tweet_content = models.CharField(max_length=200)

    def __str__(self):
        return self.tweet_content
