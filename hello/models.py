from django.db import models
from django.db.models import CheckConstraint
from PIL import Image

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)
