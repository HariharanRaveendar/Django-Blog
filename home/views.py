from django.shortcuts import render
from .models import ArticleCategorty,ArticleSubCategorty
from myarticles.models import MyArticle
from comments.models import Comments
from datetime import date,timedelta
from readarticle.views import name


# Create your views here.
def home(request):
    data = {}
    data['subcategory']=ArticleSubCategorty.objects.all()
    data['category']= ArticleCategorty.objects.all()
    data['pop'] = name()
    # data['Eng'] = ArticleSubCategorty.objects.filter(CategoryName=ArticleCategorty.objects.get(CategoryName="Engineering"))
    # data['Trav'] = ArticleSubCategorty.objects.filter(
    #     CategoryName=ArticleCategorty.objects.get(CategoryName="Travell"))
    # data['Gen'] = ArticleSubCategorty.objects.filter(
    #     CategoryName=ArticleCategorty.objects.get(CategoryName="General"))

    datehome = date.today()-timedelta(days=7)
    data['read']=MyArticle.objects.filter(DatePublished__gt=datehome)
    return render(request,'home/index.html',data)
