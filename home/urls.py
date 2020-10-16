
from django.urls import path, include
from . import views
from .views import HomeView, ArticleDetailView, CreatePostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, LikeView, AddCommentView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name = 'article_details'),
    path('contact/', views.contact, name = 'contact'),
    path('about/', views.about, name = 'about'),
    path('createArticle', CreatePostView.as_view(), name = 'create_post'),
    path('add_category', AddCategoryView.as_view(), name = 'add_category'),
    path('category/<slug:slug>/', CategoryView, name = 'category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name = 'edit'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name = 'del_post'),
    path('like/<int:pk>', LikeView, name = 'like_post'),
    #path('article/<int:pk>/comment', CommentView, name = 'comment_post'),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name = 'post_comment'),

]
