from django.contrib import admin
from django.urls import path,re_path,include
from . import views

urlpatterns = [

    path('addcomment/<int:id>',views.addcomment,name='addcomment'),

]