from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        return str(self.pub_date >= timezone.now() - datetime.timedelta(days=1))
    def __str__(self):
        return str(self.question_text),' - ',str(self.pub_date)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return str(self.question),' - ',str(self.choice_text),' - ',self.votes