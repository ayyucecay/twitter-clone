from django.db import models


class TopicsFollow(models.Model):
    topic_name = models.CharField(max_length=20)
    id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return self.topic_name
