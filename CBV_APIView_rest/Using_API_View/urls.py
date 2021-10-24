
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Using_API_View import views


urlpatterns = [
    path('transformers_details/', views.TransList.as_view()),
    path('transformers/<int:pk>', views.TransDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)