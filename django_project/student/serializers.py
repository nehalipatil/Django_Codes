from rest_framework import serializers
#from django.core.serializers import serialize   import method for Django
from student.models import Student

class StudentSerializer(serializers.ModelSerializer):
    # Specify "username" field below will override the "username" of the model or you can add extra fields to a
    # ModelSerializer as per your needs.
    # username = serializers.CharField(read_only=True)
    # this extra field will not get save into DB but will show in response
    class Meta:
        model = Student
        fields = '__all__'
        # if we want only specific fields then Specific fields to be returned to the response
        # fields = ['username', 'password', 'is_active']

