from rest_framework import viewsets
from .serializers import NoteSerializer
from .models import Notes
from tags.models import Tags
from django.db.models import Prefetch

class NotesViewset(viewsets.ModelViewSet):

    serializer_class = NoteSerializer

    def get_queryset(self):
        user = self.request.user
        notes = Notes.objects.filter(user= user).prefetch_related('tags')
        return notes
    
    def perform_create(self, serializer):
        #save note with user
        note = serializer.save(user= self.request.user)

        # check has tags and if tags has then set tags in note
        tags = self.request.data.get('tags', '')
        tags_name = []
        if(tags):
            tags = tags.lower().split(',')
            for tag_name in tags:
                tag, create = Tags.objects.get_or_create(name= tag_name, user= self.request.user)
                tags_name.append(tag)

        note.tags.set(tags_name)
        return note