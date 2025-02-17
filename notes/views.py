from rest_framework import viewsets
from .serializers import NoteSerializer
from .models import Notes

class NotesViewset(viewsets.ModelViewSet):
    serializer_class = NoteSerializer

    def get_queryset(self):
        user = self.request.user
        notes = Notes.objects.filter(user= user)
        return notes