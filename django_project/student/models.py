from django.db import models

class Student(models.Model):
    username = models.CharField(db_column='username',max_length=100, blank=False, null=False)
    password = models.TextField(blank=False, null=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)#date,integer

    class Meta:
        db_table = "student"
