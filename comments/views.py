from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from comments.models import Comments,Reply,Like
from myarticles.models import MyArticle
import json

# Create your views here.
def links(request):
    return render(request,'admin/links.html')


def savecomments(request,id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            cname = request.user.first_name
            cemail = request.user.email
            if json.loads(request.POST['commentssave']):
                cmessage = json.loads(request.POST['cmessage'])
                cmd= Comments(
                    CommentorName=cname,
                    CommentorEmail=cemail,
                    CommentorComments=cmessage,
                    ArticleId=MyArticle.objects.get(pk=id)
                )
                cmd.save()
                return JsonResponse({
                    'CommentorName': cname,
                    'CommentorComments': cmessage,
                    'id':cmd.id
                    })
        else:
            if json.loads(request.POST['commentssave']):
                cname = json.loads(request.POST['cname'])
                cemail = json.loads(request.POST['cemail'])
                cmessage = json.loads(request.POST['cmessage'])
                cmd = Comments.objects.create(
                    CommentorName=cname,
                    CommentorEmail=cemail,
                    CommentorComments=cmessage,
                    ArticleId=MyArticle.objects.get(pk=id)
                )
                cmd.save()
                return JsonResponse({
                    'msg':'save successfully',
                    'CommentorName': cname,
                    'CommentorComments': cmessage,
                    'id': cmd.id
                })
    return JsonResponse({
        'a':id
    })


def savereply(request,id):
    if request.method == 'POST':
        if json.loads(request.POST['replyrecive']):
            a=Comments.objects.get(pk=id)
            return JsonResponse({
                'a':a.id,
                'commentsname':a.CommentorName
            })
        elif json.loads(request.POST['sendreply']):
            if request.user.is_authenticated:
                rname=request.user.first_name
                remail =request.user.email
                rmessage = json.loads(request.POST['rmessage'])
                Reply.objects.create(
                    ReplyName=rname,
                    ReplyEmail=remail,
                    ReplyComments=rmessage,
                    CommentId=Comments.objects.get(pk=id),
                    ArticleId=Comments.objects.get(pk=id).ArticleId
                )
                return JsonResponse({
                    'msg':'reply sent Successfully'
                })
            else:
                rname = json.loads(request.POST['rname'])
                remail = json.loads(request.POST['remail'])
                rmessage = json.loads(request.POST['rmessage'])
                Reply.objects.create(
                    ReplyName=rname,
                    ReplyEmail=remail,
                    ReplyComments=rmessage,
                    CommentId=Comments.objects.get(pk=id),
                    ArticleId=Comments.objects.get(pk=id).ArticleId
                )
                return JsonResponse({
                    'msg': 'save successfully'
                })
        elif json.loads(request.POST['viewreply']): 
            object = Reply.objects.filter(CommentId=id,ArticleId=Comments.objects.get(pk=id).ArticleId)
            data={'obj':[]}
            data['id']=id
            for obj in object:
                temp ={}
                temp['username']=obj.ReplyName
                temp['comments']=obj.ReplyComments
                data['obj'].append(temp)

            return JsonResponse(data)


def savelike(request,id):
    if request.method == 'POST':
        if json.loads(request.POST['like']):
            Like.objects.create(
                Likes=True,
                ArticleId=MyArticle.objects.get(pk=id)
            )
        return JsonResponse(
            {'count':Like.objects.filter(ArticleId=id).count()}
        )


