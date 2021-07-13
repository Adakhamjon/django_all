from django.urls import path
from .views import*
urlpatterns = [
	path("",all_music,name = "home-page"),
	path("<int:_id>/",single_music),

]