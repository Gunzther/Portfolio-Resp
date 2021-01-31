import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, default="")
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
