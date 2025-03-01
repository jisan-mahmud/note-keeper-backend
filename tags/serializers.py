from rest_framework import serializers 
from .models import Tags

class TagSerializers(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = ['id', 'name']