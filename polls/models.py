import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    # 첫 번째 위치 인수 -> 이름 지정및 내부 설명 용도
    pub_date = models.DateTimeField('date published')
    total = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # Question 테이블과의 외래키 설정(Question테이블에서 해당 field삭제 시 Choice테이블에서 함께 적용된다.)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def __str__(self):
        return self.choice_text
