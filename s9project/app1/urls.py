from django.urls import path
from . import views
urlpatterns = [
        path('', views.mainhome,name='mainhome'),
path('login/',views.login,name='login'),
path('error/',views.error,name='error'),
        path('home/',views.home,name='home'),
        path('contact/',views.contact,name='contact'),
        path('menu/',views.menu,name='menu'),
        path('table/',views.table,name='table'),
        path('about/',views.about,name='about'),
        path('mainhome/', views.mainhome,name='mainhome'),
  ]
