from django.db import models

class Quiz(models.Model):
    quiz_no = models.IntegerField(auto_created=True, primary_key=True)
    content = models.CharField(max_length=150, blank=True, null=True)
    answer = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'quiz'


class Results(models.Model):
    result_no = models.IntegerField(auto_created=True, primary_key=True)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'results'
