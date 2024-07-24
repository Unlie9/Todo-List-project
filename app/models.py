from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Task(models.Model):
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
