from django.db import models
from users.models import CustomUser
from .validators import validate_file_extension
import uuid
from django.utils import timezone
from django.shortcuts import reverse
# Create your models here.

class File(models.Model):
    CHOICES = (
        ('1', 'public'),
        ('2', 'private'),
   
)
    id = models.UUIDField(
        primary_key= True,
        default = uuid.uuid4,
        editable = False
    )
    title = models.CharField(max_length=100, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails', null=True)
    file = models.FileField(upload_to='files', null=True,  validators=[validate_file_extension])
    description = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(default=timezone.now)
    option = models.CharField(max_length=200, null=True, choices=CHOICES, default='public')
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self, **kwargs):
        return reverse('file_detail', kwargs={'pk':self.pk})

class Contact(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30, null=True)
    text = models.TextField(null=True)

