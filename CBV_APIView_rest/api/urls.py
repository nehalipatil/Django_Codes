from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views


urlpatterns = [
    path('student_details/', views.StudentAPI.as_view()),
    path('student_byid/<int:pk>', views.StudentAPI.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)