from django.db import models

class Paste(models.Model):
    title = models.CharField(max_length=200)
    public = models.BooleanField()
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    key = models.CharField(max_length=15)

class Comment(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')
    paste = models.ForeignKey(Paste)
