import uuid

from django.db import models

class User(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created = models.DateTimeField(auto_now=True)
    email = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
