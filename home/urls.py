
from django.urls import path, include
from . import views
from .views import HomeView, ArticleDetailView, CreatePostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

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
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
