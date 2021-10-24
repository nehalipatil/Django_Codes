from django.db import models


# Create your models here.
class Faculty(models.Model):
    fno = models.IntegerField()
    f_name = models.CharField(max_length=64)
    f_sal = models.FloatField()
    f_city = models.CharField(max_length=64)


    class Meta:
        db_table = "faculty"

    def __str__(self):
        return self.f_name


from django.db import models

# Create your models here.
