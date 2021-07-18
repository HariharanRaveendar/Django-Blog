from django.urls import path
from . import views
urlpatterns = [
    path('admindash/', views.admindash, name="admindash"),
    path('datatables/', views.datatables, name="datatables"),

    path('addcategory/', views.addcategory, name="addcategory"),
    path('updatecategory/<int:id>/', views.updatecategory, name="updatecategory"),
    path('deletecategory/<int:id>/', views.deletecategory, name="deletecategory"),

    path('addsubcategory/', views.addsubcategory, name="addsubcategory"),
    path('updatesubcategory/<int:id>/',views.updatesubcategory, name="updatesubcategory"),
    path('deletesubcategory/<int:id>/',
         views.deletesubcategory, name="deletesubcategory"),

    path('addarticle/', views.addarticle, name="addarticle"),
    path('updatearticle/<int:id>/<str:path>/', views.updatearticle, name="updatearticle"),
    path('deletearticle/<int:id>/',
         views.deletearticle, name="deletearticle"),

    path('category/', views.category, name="category"),
    path('subcategory/', views.subcategory, name="subcategory"),
    path('article/', views.article, name="article"),
    path('usersettings', views.usersettings, name="usersettings"),
]
