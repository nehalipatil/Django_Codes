# GenericAPIView and Model Mixin
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

class StudentList(GenericAPIView, ListModelMixin):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer

 def get(self, request, *args, **kwargs):
  return self.list(request, *args, **kwargs)

class StudentCreate(GenericAPIView, CreateModelMixin):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer

 def post(self, request, *args, **kwargs):
  return self.create(request, *args, **kwargs)

class StudentRetrive(GenericAPIView, RetrieveModelMixin):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer

 def get(self, request, *args, **kwargs):
  return self.retrieve(request, *args, **kwargs)

class StudentUpdate(GenericAPIView, UpdateModelMixin):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer

 def put(self, request, *args, **kwargs):
  return self.update(request, *args, **kwargs)

class StudentDestroy(GenericAPIView, DestroyModelMixin):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer

 def delete(self, request, *args, **kwargs):
  return self.destroy(request, *args, **kwargs)
 ##############################################################################
 """
 post and get     ...............> get,put delete by id 
 """
 class StudentListCreate(GenericAPIView,ListModelMixin,CreateModelMixin):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

  def get(self,request,*args,**kwargs):
   return self.list(request,*args,**kwargs)
  def post(self,request,*args,**kwargs):
   return self.create(request,*args,**kwargs)

class StudentRetriveUpdateDistroy(GenericAPIView, RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer

 def get(self, request, *args, **kwargs):
  return self.retrieve(request, *args, **kwargs)
 def put(self, request, *args, **kwargs):
  return self.retrieve(request, *args, **kwargs)
 def delete(self, request, *args, **kwargs):
  return self.retrieve(request, *args, **kwargs)