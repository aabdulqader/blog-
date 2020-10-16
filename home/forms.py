from django import forms
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name','name')

choices_list = []
for item in choices:
    choices_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag','category','author', 'body','snippet', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Title Name'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Title Tag' }),
            'category': forms.Select( choices=choices_list, attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control','value':'', 'id':'elder', 'type':'hidden' }),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descriptions'}),
            'snippet': forms.TextInput(attrs={'class':'form-control'}),

        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body','snippet', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Title Name'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Title Tag' }),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descriptions'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),

        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email','message')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Name'}),
            'email': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Valid Email' }),
            'message': forms.Textarea(attrs={'class':'form-control', 'placeholder':'message'}),

        }

        


