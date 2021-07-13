from django.urls import path
from .views import*
urlpatterns = [
	path("movies/",all_movies),
	path("/1",single_movie),

]