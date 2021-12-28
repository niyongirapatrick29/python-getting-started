from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "Movie Library"
admin.site.site_title = "Movie Library"
admin.site.index_title = "Welcome to Movie Library Portal"

admin.site.register(Genre);
admin.site.register(Actor);
admin.site.register(Movie);