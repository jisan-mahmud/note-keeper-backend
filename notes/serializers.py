from rest_framework import serializers
from .models import Notes

class NoteSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    class Meta:
        model = Notes
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
            'tags': {'ready_only': True}
        }


    def get_tags(self, obj):
        return [tag.name for tag in obj.tags.all()]