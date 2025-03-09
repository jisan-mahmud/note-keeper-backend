from django.db import models
from accounts.models import User
from tags.models import Tags
from uuid import uuid4

class Notes(models.Model):
    id = models.UUIDField(default= uuid4, primary_key=True, editable= False)
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'user_note')
    tags = models.ManyToManyField(Tags, related_name= 'tags_note', blank= True)
    title = models.CharField(max_length= 300)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f'id: {self.id} - title: {self.title}'
    

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'

    
