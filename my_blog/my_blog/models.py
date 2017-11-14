
from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=20)
    abstract = models.CharField(max_length=100)
    emojiId = models.IntegerField(default=0)
    mdFileName = models.CharField(max_length=50)
    createTime = models.IntegerField(default=0)

    class Meta:
        db_table = 'articles'

class Emojis(models.Model):
    emojiName = models.CharField(max_length=50,unique=True)

    class Meta:
        db_table = 'emojis'