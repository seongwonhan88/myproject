from django.urls import path

from . import views

urlpatterns=[
    path('login/', views.login_view, name='login_view'),
    path('signin/', views.signin_view, name='signin-view'),
]