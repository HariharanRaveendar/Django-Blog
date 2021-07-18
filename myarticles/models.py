from django.db import models
from home.models import ArticleCategorty, ArticleSubCategorty
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class MyArticle(models.Model):
    CategoryName = models.ForeignKey(
        ArticleCategorty, on_delete=models.CASCADE)
    SubCategoryName = models.ForeignKey(
        ArticleSubCategorty, on_delete=models.CASCADE)
    Title = models.CharField(max_length=200)
    Img = models.ImageField(upload_to='pics',null=True)
    File = models.FileField(upload_to='docs/',null=True)
    Subject = models.TextField()
    SubTitle = models.CharField(max_length=200)
    Body = RichTextField(config_name='awesome_ckeditor')
    DatePublished = models.DateField(
        auto_now_add=True, verbose_name='Published on')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title
    def delete(self, *args, **kwargs):
        self.Img.delete()
        self.File.delete()
        super().delete(*args, **kwargs)
