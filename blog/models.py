from django.db import models

# Create your models here.
class BlogPost(models.Model):
    # id =models.IntegerField()
    title = models.CharField(max_length=120)
    content = models.TextField(null=True, blank=True)
    slug =  models.SlugField(unique=True) # change value "hello world" --> "hello-world"



