from django.urls import path
from . import views
urlpatterns = [
    path('<int:sid>/', views.articles, name="articles")
]

