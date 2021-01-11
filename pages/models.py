from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=200,null=True)
    description = models.TextField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    playstore_link = models.CharField(max_length=200,null=True)
    appstore_link = models.CharField(max_length=200,null=True)
    website_link = models.CharField(max_length=200,null=True)
    product_pictures = models.ImageField(upload_to='products/')
    date_created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Blog(models.Model):
    heading = models.CharField(max_length=200,null=True)
    subheading = models.CharField(max_length=200,null=True)
    description = models.TextField(null=True, blank=True)
    website_link = models.CharField(max_length=200,null=True)
    blog_pictures = models.ImageField(upload_to='blog/')
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading