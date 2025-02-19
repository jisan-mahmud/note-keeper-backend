from rest_framework.generics import ListAPIView
from .serializers import TagSerializers
from .models import Tags

class TagsListAPIView(ListAPIView):
    serializer_class = TagSerializers

    def get_queryset(self):
        query_set = Tags.objects.filter(user= self.request.user)
        return query_set