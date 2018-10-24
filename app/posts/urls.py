from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='posts'),
    path('create/', views.post_create, name='post-create')
]