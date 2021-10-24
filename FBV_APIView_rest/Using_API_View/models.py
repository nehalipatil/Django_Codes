from django.db import models

# Create your models here.
class CategoryAV(models.Model):
    category_name = models.CharField(max_length=10,blank=False,unique=True,null=False)

    class Meta:
        db_table = "CategoryAV"

class SubCategoryAV(models.Model):
    sub_category_name = models.CharField(max_length=10,blank=False,unique=True,null=False)
    category_av = models.ForeignKey(CategoryAV,on_delete=models.CASCADE,related_name="sub_category")
    #on_delete : if we are deleting somthing from main table it will be automatically deleted from child table
    # related name is forming reverse relation with main table ie. here it is forming reverse relation with "CategoryAV"
    class Meta:
        db_table = "SubCategoryAV"

class DeliveryAV(models.Model):
    Delivery_Address = models.TextField(blank=False,null=False)
    category_av = models.OneToOneField(CategoryAV,on_delete=models.CASCADE,related_name="delivery")
    class Meta:
        db_table = "DeliveryAV"

class VendorAV(models.Model):
    vendor_name = models.CharField(max_length=10,blank=False,unique=True,null=False)
    category_av = models.ManyToManyField(CategoryAV,related_name="vendor")
    class Meta:
        db_table = "VendorAV"

