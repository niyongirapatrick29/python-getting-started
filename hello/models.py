from django.db import models
from django.db.models import CheckConstraint, Q, F
from PIL import Image

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


# Create your models here.

class Genre(models.Model):  
    genreId = models.AutoField( primary_key=True, serialize=True)  
    name = models.CharField(max_length=100)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:  
        db_table = "genre"
    def __str__(self):
        return "{}".format(self.name)

class Actor(models.Model):  
    actorId = models.AutoField( primary_key=True, serialize=True)  
    fname = models.CharField(max_length=100)  
    lname = models.CharField(max_length=100)
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.IntegerField(choices=GENDER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:  
        db_table = "movie_actors"
    def __str__(self):
        return "{} - {} - {}".format(self.fname, self.lname, self.gender)

class Movie(models.Model):  
    movieId = models.AutoField( primary_key=True, serialize=True)  
    movieTitle = models.CharField(max_length=200)  
    movieActor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movieYear = models.DateField(default='2021-12-12')
    ENG = 'English'
    KINY = 'kinyarwanda'
    FR = 'French'
    LANGUAGE_CHOICES = [(ENG, 'English'), (KINY, 'kinyarwanda'), (FR, 'French')]
    movieLanguage = models.CharField(max_length=200, choices=LANGUAGE_CHOICES)
    movieGenre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    movieLogo = models.ImageField(upload_to='img/%y')
    movie_file = models.FileField(upload_to='img/%y')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:  
        db_table = "movies"
    def __str__(self):
        return "{} - {} - {}".format(self.movieTitle, self.movieActor, self.movieYear)
