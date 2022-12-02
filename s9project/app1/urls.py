from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
        path('', views.mainhome,name='mainhome'),
        path('register/',views.register,name='register'),
        path('profile/',views.profile,name='profile'),
        path('error/',views.error,name='error'),
        path('home/',views.home,name='home'),
        path('contact/',views.contact,name='contact'),
        path('menu/',views.menu,name='menu'),
        path('table/',views.table,name='table'),
        path('about/',views.about,name='about'),
        path('mainhome/', views.mainhome,name='mainhome'),
        path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
        path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
  ]
