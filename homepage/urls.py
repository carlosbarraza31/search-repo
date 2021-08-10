from django.urls import path
from . import views

app_name = "homepage"
urlpatterns = [
    path("", views.index, name = 'index'),
    path("imageSearch", views.imageSearch, name = "imageSearch"),
    path("advancedSearch", views.advancedSearch, name = "advancedSearch")
]