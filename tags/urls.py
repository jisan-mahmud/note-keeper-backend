from django.urls import path
from .views import TagsListAPIView
urlpatterns = [
    path('', TagsListAPIView.as_view(), name= 'user-tags')
]
