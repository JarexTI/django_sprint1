from django.urls import path


app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:id>/', views.post_datail, name='blog'),
    path('category/<slug:category_slug>/', views.category_posts, name='blog')
]
