from rest_framework import serializers
from django.urls import reverse
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
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        words = data['note'].split()

        if len(words) > 20:
            data['note'] = " ".join(words[:20]) + '...'
        else:
            data['note'] = " ".join(words) 
            
        data['link'] = {
            'self': reverse('notes-detail', kwargs={'pk': data.get('id')})
        }
        
        return data