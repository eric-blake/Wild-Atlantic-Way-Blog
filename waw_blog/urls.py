from . import views
from django.urls import path
from waw_blog.views import blog, about


urlpatterns = [
    path("about/", about, name='about'),
    path("", blog, name='home'),
    path('post_create/', views.PostCreate.as_view(), name='post_create'),
    path('post_update/<slug:slug>', views.PostUpdate.as_view(),
         name='post_update'),
    path('post_delete/<slug:slug>', views.PostDelete.as_view(),
         name='post_delete'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('category/<slug:category_slug>/', views.post_filter,
         name='category_filter'),
]
