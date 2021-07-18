from django.shortcuts import render
from home.models import ArticleCategorty, ArticleSubCategorty
from myarticles.models import MyArticle
from django.conf import settings
# Create your views here.


def articles(request,sid):
    data={}
    subobj = ArticleSubCategorty.objects.get(pk=sid)
    data['subcategoryname']= subobj.SubCategoryName
    data['subcategorydesc'] = subobj.SubCategoryDesc
    # data['Eng'] = ArticleSubCategorty.objects.filter(
    #     CategoryName=ArticleCategorty.objects.get(CategoryName="Engineering"))
    # data['Trav'] = ArticleSubCategorty.objects.filter(
    #     CategoryName=ArticleCategorty.objects.get(CategoryName="Travell"))
    # data['Gen'] = ArticleSubCategorty.objects.filter(
    #     CategoryName=ArticleCategorty.objects.get(CategoryName="General"))
    data['categoryname'] = subobj.CategoryName.CategoryName
    newsobj = MyArticle.objects.filter(
        SubCategoryName=sid).only('Title', 'Img', 'Subject','id')
    data['newsfeed']=newsobj


    return render(request, 'myarticles/myarticles.html',data)
