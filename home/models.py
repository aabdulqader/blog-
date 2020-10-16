from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

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
    #body = models.TextField()
    body = RichTextField(blank=True, null=True)
    snippet = RichTextField(blank=True, null=True)
    image = models.ImageField( default='default_post_img.jpg',blank=True, null=True,upload_to='images/' )
    time = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

 
    

    def total_likes(self):
        return self.likes.count()



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




class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(default = 'default.jpg', null=True, blank=True,upload_to='profile_pic/' )
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return str(self.user)


    


    




class Comment(models.Model):
    post = models.ForeignKey(Post, related_name = "comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=225)
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_added"]


    def __str__(self):
        return "%s - %s" % (self.post.title, self.name)

    
    def get_absolute_url(self):
        #return reverse("article_details", kwargs={"pk": self.pk})
        return reverse("home")
    

