from django import forms
from .models import Post, Category

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
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descriptions'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),

        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body','snippet', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Title Name'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Title Tag' }),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descriptions'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),

        }


