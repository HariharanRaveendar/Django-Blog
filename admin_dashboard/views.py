from django.shortcuts import render,redirect
from myarticles.models import MyArticle
from contact.models import Subscription
from home.models import ArticleCategorty,ArticleSubCategorty
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse,JsonResponse
from django.core.serializers import serialize
from django.core.mail import send_mail
from admin.settings import EMAIL_HOST_USER
import json

# Create your views here.
#views for Admindashboard
def admindash(request):
    data={}
    data['category'] = ArticleCategorty.objects.all().order_by('id')
    data['subcategory'] = ArticleSubCategorty.objects.all().order_by('id')
    data['article'] = MyArticle.objects.all().order_by('id')
    return render(request,'admin/dashboard.html',data)

def datatables(request):
    data = {}
    data['category'] = ArticleCategorty.objects.all().order_by('id')
    data['subcategory'] = ArticleSubCategorty.objects.all().order_by('id')
    data['article'] = MyArticle.objects.all().order_by('id')
    return render(request,'admin/datatables.html',data)


def usersettings(request):
    return render(request, 'admin/usersettings.html')
#endviews for Admindashboard
###################################################################################################################
#views for category,article,subcategory,links
def category(request):
    data = {}
    data['category'] = ArticleCategorty.objects.all().order_by('id')
    return render(request, 'admin/addcategory.html', data)

def subcategory(request):
    data = {}
    data['category'] = ArticleCategorty.objects.all()
    data['subcategory'] = ArticleSubCategorty.objects.all().order_by('id')
    return render(request, 'admin/addsubcategory.html', data)

def article(request):
    data={}
    data['category'] = ArticleCategorty.objects.all().order_by('id')
    data['subcategory'] = ArticleSubCategorty.objects.all().order_by('id')
    data['article'] = MyArticle.objects.all().order_by('id')
    data['user'] = User.objects.all().order_by('id')
    return render(request, 'admin/addarticle.html',data)

#End views for category,article,subcategory,links
####################################################################################################################
#views for addcategory,addarticle,addsubcategory,links
def addcategory(request):
    data={}
    if request.method == 'POST':
        category = request.POST['category']
        if ArticleCategorty.objects.filter(CategoryName=category).exists():
            data['msg']="Category Name Already Exists"
            data['category'] = ArticleCategorty.objects.all().order_by('id')
            return render(request,'admin/category.html',data)
        else:
            ArticleCategorty.objects.create(
            CategoryName=category
        ).save()
        return redirect('category')
    else:
        return redirect('category')

def addsubcategory(request):
    if request.method == 'POST':
        category = ArticleCategorty.objects.get(pk=request.POST['category'])
        subcategory = request.POST['subcategory']
        subdesc = request.POST['subdesc']
        # print(category, subcategory, subdesc)

        subcat = ArticleSubCategorty.objects.create(
            CategoryName=category,
            SubCategoryName=subcategory,
            SubCategoryDesc=subdesc
        )
        subcat.save()
        return redirect('subcategory')
    else:
        return redirect('subcategory')

def addarticle(request):
    if request.method == 'POST':
        category = ArticleCategorty.objects.get(pk=request.POST['category'])
        subcategory = ArticleSubCategorty.objects.get(
            pk=request.POST['subcategory'])
        user = User.objects.get(pk=request.POST['user'])
        title = request.POST['title']

        subtitle = request.POST['subtitle']
        subject = request.POST['subject']
        body = request.POST['bodycontent']
        try:
            docs = request.FILES.get('docs')
        except:
            docs = None
        try:
            img = request.FILESget('img')
        except:
            img = None

        MyArticle.objects.create(
            CategoryName=category,
            SubCategoryName=subcategory,
            user=user,
            Title=title,
            Img=img,
            SubTitle=subtitle,
            Subject=subject,
            Body=body,
            File=docs
        ).save()
        email(title)
        return redirect('article')

def email(title):
    obj = MyArticle.objects.get(Title=title)
    mail= Subscription.objects.all()
    l = []
    for i in mail:
        l.append(i.SubcriberEmail)
    sub=title
    body = "New Article Written by authon plse go and view this article through this link http://127.0.0.1:8000/read/"+str(obj.id)+"/"
    send_mail(sub,body,EMAIL_HOST_USER,l,fail_silently=False)
#endviews for addcategory,addarticle,addsubcategory,links
###################################################################################################################
#views for Updatecategory,Updatearticle,updatesubcategory,updatelinks
def updatecategory(request,id):
    if request.method=="POST":
        if json.loads(request.POST['category']):
            a = ArticleCategorty.objects.get(pk=id)
            return JsonResponse({
                'id':a.id,
                'cname':a.CategoryName
            })
        elif json.loads(request.POST['updcategory']):
            a = json.loads(request.POST['cname'])
            if ArticleCategorty.objects.filter(CategoryName=a).exists():
                return JsonResponse({'err':'Category Already Exists'})
            else:
                ArticleCategorty.objects.filter(id=id).update(CategoryName=a)
                return JsonResponse({
                    'id': id,
                    'cname': a,
                    'err':0
                })
def updatesubcategory(request,id):
    if request.method == 'POST':
        if json.loads(request.POST['subcategory']):
            s = ArticleSubCategorty.objects.get(pk=id)
            ls=ArticleCategorty.objects.all()
            cat=[]
            for l in ls:
                cat.append(l.CategoryName)

            return JsonResponse({
                'id':s.id,
                'sname':s.SubCategoryName,
                'sdesc':s.SubCategoryDesc,
                'cname':s.CategoryName.CategoryName,
                'cat':cat
            })
        elif json.loads(request.POST['updsubcategory']):
            sname = json.loads(request.POST['sname'])
            cname = json.loads(request.POST['cname'])
            sdesc = json.loads(request.POST['sdesc'])

            if ArticleSubCategorty.objects.filter(SubCategoryName__iexact=sname).exclude(id=id).exists():
                return JsonResponse({
                    "err":"SubcategoryName Already Exsits"
                })
            else:
                cid = ArticleCategorty.objects.filter(CategoryName=cname).first()
                ArticleSubCategorty.objects.filter(pk=id).update(
                    CategoryName=cid,
                    SubCategoryName=sname,
                    SubCategoryDesc=sdesc
                )
                return JsonResponse({
                    'err':0,
                    'id':id,
                    'sname':sname,
                })
    return JsonResponse({
        'a': s
    })

def updatearticle(request,id, path):
    if request.method =='POST':
        a = MyArticle.objects.get(pk=id)
        try:
            i=request.FILES['img']
            if a.Img.name != "":
                a.Img.delete()
            a.Img=i
            a.save()
        except:
            i=a.Img
        try:
            d = request.FILES['docs']
            if a.File.name != "":
                a.File.delete()
            a.File=d
            a.save()
        except:
            d=a.File
        category = ArticleCategorty.objects.get(pk=request.POST['category'])
        subcategory = ArticleSubCategorty.objects.get(pk=request.POST['subcategory'])
        user = User.objects.get(pk=request.POST['user'])
        title = request.POST['title']
        subtitle = request.POST['subtitle']
        subject = request.POST['subject']
        body = request.POST['bodycontent']

        MyArticle.objects.filter(pk=id).update(
            CategoryName=category,
            SubCategoryName=subcategory,
            user=user,
            Title=title,
            SubTitle=subtitle,
            Subject=subject,
            Body=body
        )
        mail = Subscription.objects.all()
        l = []
        for i in mail:
            l.append(i.SubcriberEmail)
        sub = title
        body = "Update Article Written by authon plse go and view this article through this link http://127.0.0.1:8000/read/" + \
            str(id)+"/"
        send_mail(sub, body, EMAIL_HOST_USER, l, fail_silently=False)
        if path == 'article':
            return redirect('article')
        else:
            return redirect('admindash')
    else:
        data={}
        data['subcategory']= ArticleSubCategorty.objects.all()
        data['category'] = ArticleCategorty.objects.all()
        data['article']= MyArticle.objects.get(pk=id)
        data['user'] = User.objects.all()
        data['path']=path

        return render(request,'admin/updatearticle.html',data)
#endviews for Updatecategory,Updatearticle,updatesubcategory,updatelinks

def deletecategory(request,id):
    if request.method == "POST":
        if json.loads(request.POST['cdelete']):
            d = ArticleCategorty.objects.get(pk=id)
            return JsonResponse({
                'id': d.id,
                'cname': d.CategoryName
            })
        elif json.loads(request.POST['cdeletedb']):
            ArticleCategorty.objects.filter(pk=id).delete()
            return JsonResponse({
                'id':id,
                })

def deletesubcategory(request, id):
    if request.method == 'POST':
        if json.loads(request.POST['sdelete']):
            s = ArticleSubCategorty.objects.get(pk=id)
            ls = ArticleCategorty.objects.all()
            cat = []
            for l in ls:
                cat.append(l.CategoryName)
            return JsonResponse({
                'id': s.id,
                'sname': s.SubCategoryName,
                'sdesc': s.SubCategoryDesc,
                'cname': s.CategoryName.CategoryName,
                'cat': cat
            })
        elif json.loads(request.POST['sdeletedb']):
            ArticleSubCategorty.objects.filter(pk=id).delete()
            return JsonResponse({
                'id':id
                })


def deletearticle(request,id):
    if request.method == 'POST':
        MyArticle.objects.filter(pk=id).delete()
        return redirect('article')
    else:
        data = {}
        data['subcategory'] = ArticleSubCategorty.objects.all()
        data['category'] = ArticleCategorty.objects.all()
        data['article'] = MyArticle.objects.get(pk=id)
        data['user'] = User.objects.all()
        return render(request, 'admin/deletearticle.html', data)
