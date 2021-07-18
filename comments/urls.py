from django.urls import path
from . import views
urlpatterns = [
    path('links/', views.links, name="links"),
    path('savecomments/<int:id>/', views.savecomments, name="savecommentss"),
    path('savereply/<int:id>/', views.savereply, name="savereply"),
    path('savelike/<int:id>/', views.savelike, name='savelike')
]
