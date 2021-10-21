from django.contrib import admin
from django.urls import path,re_path,include
from order import views

urlpatterns = [
    path('addtoshopcart/<int:id>', views.addtoshopcart,name='addtoshopcart'),
    path('deletefromcart/<int:id>/', views.deletefromcart, name='deletefromcart'),
    path('orderproduct/', views.orderproduct, name='orderproduct'),

]
