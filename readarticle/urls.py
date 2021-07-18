from django.urls import path
from . import views
urlpatterns = [
    path('<int:rid>/', views.read, name="read")
]