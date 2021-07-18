from django.shortcuts import render
from myarticles.models import MyArticle
from home.models import ArticleCategorty,ArticleSubCategorty
from comments.models import Like
from comments.models import Comments
# Create your views here.
import operator
import itertools

def read(request,rid):
    data={}
    readobj = MyArticle.objects.get(pk=rid)
    commentsobj = Comments.objects.filter(ArticleId=rid).order_by('-id')
    data['pop'] = name()
    data['read'] =readobj
    data['comments'] = commentsobj
    # data['Eng'] = ArticleSubCategorty.objects.filter(
    #     CategoryName=ArticleCategorty.objects.get(CategoryName="Engineering"))
    # data['Trav'] = ArticleSubCategorty.objects.filter(
    #     CategoryName=ArticleCategorty.objects.get(CategoryName="Travell"))
    # data['Gen'] = ArticleSubCategorty.objects.filter(
    #     CategoryName=ArticleCategorty.objects.get(CategoryName="General"))
    data['like_count']=Like.objects.filter(ArticleId=rid).count()
    return render(request, 'read/read.html', data)

def name():
    data={}
    for obj in MyArticle.objects.all():
        count = Like.objects.filter(ArticleId=obj.id).count()
        data[obj.id]=count
    new_dic=dict(sorted(data.items(), key=operator.itemgetter(1), reverse=True))
    d = dict(itertools.islice(new_dic.items(), 3))

    return_data=[]
    for x in d:
        temp={}
        art=MyArticle.objects.get(pk=x)
        temp['id']=x
        temp['img']=art.Img
        temp['title']=art.Title
        temp['sub']=art.SubCategoryName.SubCategoryName
        return_data.append(temp)
    return return_data

