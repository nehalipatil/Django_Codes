from .models import Transformer
from rest_framework import serializers

class TransformerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transformer
        fields = '__all__'