from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class ArticleCategorty(models.Model):
    CategoryName = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.CategoryName
class ArticleSubCategorty(models.Model):
    SubCategoryName = models.CharField(max_length=100, unique=True)
    SubCategoryDesc = models.TextField()
    CategoryName = models.ForeignKey('ArticleCategorty', on_delete=models.CASCADE)
    def __str__(self):
        return self.SubCategoryName

