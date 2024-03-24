from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_posts, name='get_posts'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('new/', views.create_or_edit_post, name='new_post'),
    path('<int:pk>/edit/', views.create_or_edit_post, name='edit_post'),
    path('delete/<int:id>/', views.destroy, name='delete_post'),
]