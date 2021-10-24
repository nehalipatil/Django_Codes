"""
from  rest_framework import serializers
from Using_API_View.models import CategoryAV,SubCategoryAV,DeliveryAV,VendorAV


class SubCategoryAVSerializer(serializers.Serializer):
    class Meta:
        model = SubCategoryAV
        fields = "__all__"

class DeliveryAVSerializer(serializers.Serializer):
    class Meta:
        model = DeliveryAV
        fields = "__all__"

class VendorAVSerializer(serializers.Serializer):
    class Meta:
        model = VendorAV
        fields = "__all__"

class CategoryAVSerializer(serializers.Serializer):
    sub_category = SubCategoryAVSerializer(many=True,read_only=True)
    delivery = DeliveryAVSerializer(many=True,read_only=True)
    vendor = VendorAVSerializer(read_only=True)

    class Meta:
        model = CategoryAV
        fields = ["id","category_name","sub_category","vendor","delivery"]
"""

from rest_framework  import serializers
from Using_API_View.models import CategoryAV,SubCategoryAV,VendorAV,DeliveryAV

class SubCategoryAVSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoryAV
        fields = "__all__"

class VendorAVSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorAV
        fields = "__all__"

class DeliveryAVSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAV
        fields = "__all__"

class CategoryAVSerializer(serializers.ModelSerializer):
    # related names in models.py (sub_categories,vendors,delievery)
    sub_categories = SubCategoryAVSerializer(many=True,read_only=True)
    vendors = VendorAVSerializer(many=True, read_only=True)
    delivery = DeliveryAVSerializer(read_only=True)

    class Meta:
        model = CategoryAV
        fields = ('id','category_name','sub_categories','vendors','delivery')
