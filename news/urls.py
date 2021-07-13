from django.urls import path
from .views import*
urlpatterns= [
	path("news/",all_news),
    path("1/",single_new)
]
