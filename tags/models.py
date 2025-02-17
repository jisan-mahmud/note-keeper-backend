from django.db import models
import uuid
from accounts.models import User

class Tags(models.Model):
    id = models.UUIDField(default= uuid.uuid4, primary_key= True, editable= False)
    name = models.CharField(max_length= 100)

    def __str__(self):
        return f'id: {self.id} - name: {self.name}'