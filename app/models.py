from datetime import timedelta

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, editable=False)
    deadline = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False, blank=True, null=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['done', '-creation_date']

    def deadline_time_1day(self):
        self.deadline = self.creation_date + timedelta(days=1)
        return self.deadline
