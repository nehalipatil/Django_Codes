from django.db import models



class Transformer(models.Model):
    T_name = models.CharField(db_column='T_name',max_length=100)
    T_type = models.TextField()
    T_vtg = models.IntegerField()


    class Meta:
        db_table = "transformer"

