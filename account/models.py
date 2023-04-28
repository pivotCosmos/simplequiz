from django.db import models

class Users(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    reg_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
