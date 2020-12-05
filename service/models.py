from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Identification(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	id_card_img = models.ImageField(upload_to='images/img_card/', blank=True, null=True)
	selfie_img = models.ImageField(upload_to='images/img_selfie/', blank=True, null=True)
