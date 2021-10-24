from django.contrib import admin
from django.urls import path
from Using_API_View import views

urlpatterns = [
    path('category_AV', views.category_av_list),#[get,post]
    path('category_AV_id/<int:pk>', views.category_av_details),#[put,delete,get]
    path('subcategory_AV', views.subcategory_av_list),#[get,post]
    path('subcategory_AV_id/<int:pk>', views.subcategory_av_details), #[put,delete,get]
    path('Delivery_AV', views.Delivery_av_list),#[get,post]
    path('Vendor_AV', views.Vendor_av_list)#[get,post]


]
