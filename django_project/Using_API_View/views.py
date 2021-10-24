from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Using_API_View.models import CategoryAV,SubCategoryAV,DeliveryAV,VendorAV
from Using_API_View.serializer import CategoryAVSerializer,SubCategoryAVSerializer,DeliveryAVSerializer,VendorAVSerializer



# Create your views here.
@api_view(["GET","POST"])
def category_av_list(request):
    if request.method == "GET":
        category_av = CategoryAV.objects.all()
        category_av_serializer = CategoryAVSerializer(category_av , many=True)
        return Response(category_av_serializer.data,status=status.HTTP_200_OK)
    elif request.method == "POST":
        category_av_serializer = CategoryAVSerializer(data=request.data)
        if category_av_serializer.is_valid():
            category_av_serializer.save()
            return Response(category_av_serializer.data,status=status.HTTP_201_CREATED)
        return Response(category_av_serializer.errors,status=status.HTTP_204_NO_CONTENT)

@api_view(["GET","PUT","DELETE"])
def category_av_details(request,pk):
    try:
        category_av = CategoryAV.objects.get(pk=pk)

    except CategoryAV.DoesNotExist:
        return Response(category_av.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        category_av_serializer = CategoryAVSerializer(category_av)
        return Response(category_av_serializer.data,status=status.HTTP_200_OK)

    elif request.method == "PUT":
        category_av_serializer = CategoryAVSerializer(category_av,data=request.data)
        if category_av_serializer.is_valid():
            category_av_serializer.save()
            return Response(category_av_serializer.data)
        return Response(category_av_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        category_av.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

###############################################################################################################
@api_view(["GET","POST"])
def subcategory_av_list(request):
    if request.method == "GET":
        subcategory_av = SubCategoryAV.objects.all()
        subcategory_av_serializer = SubCategoryAVSerializer(subcategory_av , many=True)
        return Response(subcategory_av_serializer.data,status=status.HTTP_200_OK)
    elif request.method == "POST":
        subcategory_av_serializer = SubCategoryAVSerializer(data=request.data)
        if subcategory_av_serializer.is_valid():
            subcategory_av_serializer.save()
            return Response(subcategory_av_serializer.data,status=status.HTTP_201_CREATED)
        return Response(subcategory_av_serializer.errors,status=status.HTTP_204_NO_CONTENT)

@api_view(["GET","PUT","DELETE"])
def subcategory_av_details(request,pk):
    try:
        subcategory_av = SubCategoryAV.objects.get(pk=pk)

    except:
        return Response(subcategory_av.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        subcategory_av_serializer = SubCategoryAVSerializer(subcategory_av)
        return Response(subcategory_av_serializer.data,status=status.HTTP_200_OK)

    elif request.method == "PUT":
        subcategory_av_serializer = SubCategoryAVSerializer(subcategory_av,data=request.data)
        if subcategory_av_serializer.is_valid():
            subcategory_av_serializer.save()
            return Response(subcategory_av_serializer.data)
        return Response(subcategory_av_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        subcategory_av.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#######################################################################################################################
@api_view(["GET","POST"])
def Delivery_av_list(request):
    if request.method == "GET":
        Delivery_av = DeliveryAV.objects.all()
        Delivery_av_serializer = DeliveryAVSerializer(Delivery_av , many=True)
        return Response(Delivery_av_serializer.data,status=status.HTTP_200_OK)
    elif request.method == "POST":
        Delivery_av_serializer = DeliveryAVSerializer(data=request.data)
        if Delivery_av_serializer.is_valid():
            Delivery_av_serializer.save()
            return Response(Delivery_av_serializer.data,status=status.HTTP_201_CREATED)
        return Response(Delivery_av_serializer.errors,status=status.HTTP_204_NO_CONTENT)
########################################################################################################
@api_view(["GET","POST"])
def Vendor_av_list(request):
    if request.method == "GET":
        Vendor_av = VendorAV.objects.all()
        Vendor_av_serializer = VendorAVSerializer(Vendor_av , many=True)
        return Response(Vendor_av_serializer.data,status=status.HTTP_200_OK)
    elif request.method == "POST":
        Vendor_av_serializer = VendorAVSerializer(data=request.data)
        if Vendor_av_serializer.is_valid():
            Vendor_av_serializer.save()
            return Response(Vendor_av_serializer.data,status=status.HTTP_201_CREATED)
        return Response(Vendor_av_serializer.errors,status=status.HTTP_204_NO_CONTENT)
##################################################################################################################
