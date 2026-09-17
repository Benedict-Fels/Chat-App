from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
