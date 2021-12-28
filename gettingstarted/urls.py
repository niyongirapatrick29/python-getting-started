from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
#from django.conf.urls import url

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("movies/", hello.views.home, name="home"),
    path("admin/", admin.site.urls),
    path('movieDetails/<int:movieId>/', hello.views.movieDetail, name="movieDetail"),

    #path(r'^img/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}), 
    #path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
#if settings.DEBUG:
    #urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)