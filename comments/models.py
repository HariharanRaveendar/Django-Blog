from django.db import models
from myarticles.models import MyArticle
# Create your models here.
class Links(models.Model):
    FaceBook = models.CharField(max_length=255,unique=True)
    Instagram = models.CharField(max_length=255, unique=True)
    Linkedin = models.CharField(max_length=255,unique=True)
    Twitter = models.CharField(max_length=255, unique=True)
class Comments(models.Model):
    CommentorName = models.CharField(max_length=100,unique=False)
    CommentorEmail = models.EmailField(max_length=250, unique=False)
    CommentorComments = models.TextField()
    ArticleId = models.ForeignKey(MyArticle, on_delete=models.CASCADE)
    def __str__(self):
        return self.CommentorName

class Reply(models.Model):
    ReplyName = models.CharField(max_length=100,unique=False)
    ReplyEmail = models.EmailField(max_length=250, unique=False)
    ReplyComments = models.TextField()
    CommentId = models.ForeignKey(Comments,on_delete=models.CASCADE)
    ArticleId = models.ForeignKey(MyArticle, on_delete=models.CASCADE)
    def __str__(self):
        return self.ReplyName

class Like(models.Model):
    Likes = models.BooleanField()
    ArticleId = models.ForeignKey(MyArticle, on_delete=models.CASCADE)


