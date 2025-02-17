from rest_framework import serializers
from .models import Notes

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notes
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
            'tags': {'read_only': True}
        }