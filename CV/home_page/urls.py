from django.urls import path
from . import views

urlpatterns = [ 
    path('home_page/', views.home_page, name='home_page'),
    path('home_page/exp_page/', views.exp_page, name='exp_page'),
    path('home_page/hobby_page/', views.hobby_page, name='hobby_page'),
    path('home_page/qualities_page/', views.qualities_page, name='qualities_page')
]