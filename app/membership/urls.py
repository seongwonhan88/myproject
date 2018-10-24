from django.urls import path

from . import views

app_name = 'membership'
urlpatterns=[
    path('login/', views.login_view, name='login_view'),
    path('signin/', views.signin_view, name='signin-view'),
    path('logout/', views.logout_view, name='logout-view')
]