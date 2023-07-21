from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    reg_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'users'
