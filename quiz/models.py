from django.db import models

class Quiz(models.Model):
    content = models.CharField(max_length=255, blank=True, null=True)
    answer = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'quiz'


class Result(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    quiz_id = models.IntegerField(blank=True, null=True)
    result = models.BooleanField(default=False)
    update_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'result'


class Score(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'score'
