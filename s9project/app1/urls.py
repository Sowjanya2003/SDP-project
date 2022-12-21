from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
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
        path("getres/",views.getres,name="getres"),
        path('checkuser/',views.checkuser,name="checkuser"),
        path("gettableres/",views.gettableres,name="gettableres"),
        path('addtocart/',views.addtocart,name='addtocart'),
path('addtocart2/',views.addtocart2,name='addtocart2'),

        path('payment/',views.payment,name='payment'),

  ]
