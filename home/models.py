from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, null=True )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        #return reverse("create_post", kwargs={"pk": self.pk})
        return reverse('create_post')


class Post(models.Model):

    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=50)
    category = models.CharField(max_length=200, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(default='default.jpg', blank=True)
    time = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse("article_details", kwargs={"pk": self.pk})
    

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    desc = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.name + ' | ' + self.desc   

    

