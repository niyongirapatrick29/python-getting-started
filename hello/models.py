from django.db import models
#from django.db.models import CheckConstraint
#from PIL import Image

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


class Genre(models.Model):  
    genreId = models.AutoField( primary_key=True, serialize=True)  
    name = models.CharField(max_length=100)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:  
        db_table = "genre"
    def __str__(self):
        return "{}".format(self.name)