from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .models import Post, Contact, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm,UpdateForm
from django.urls import reverse_lazy, reverse
from django.contrib import messages


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))

    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article_details', args=[str(pk)]))
    




class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']
    #ordering = ['id']

    def get_context_data(self, **kwargs):
        category_menu = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context["category_menu"] = category_menu
        return context
    

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked 
        return context
    
    

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
        message = request.POST['message']
        instance = Contact(name=name, email=email, desc=desc, message=message) 
        instance.save()
        messages.success(request, f'Thanks. We Receive Your Message SUCCESSFULLY. You\'ll reply soon.')
        return redirect('contact')
    return render (request, 'contact.html')

def about(request):
    return render (request, 'about.html')

class CreatePostView(CreateView):
    model = Post  
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title', 'body', 'image')


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
    #fields = ('title', 'body', 'image')

def CategoryView(request, slug):
    category_posts = Post.objects.filter(category=slug.replace('-', ' '))
    x = len(category_posts)
    return render (request, 'category.html', {'slug':slug,'x':x,  'category_posts':category_posts})

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'
    #fields = ['title','body','image']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'del_post.html'
    success_url = reverse_lazy('home')


