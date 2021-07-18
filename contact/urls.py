from django.urls import path
from . import views
urlpatterns = [
    path('savemessage/', views.savemessage, name="savemessage"),
    path('getsubscriber/', views.getsubscriber, name="getsubscriber"),
]
