from django.contrib import admin
from django.urls import path,re_path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('contact/',views.contact,name='contact'),
    path('about/', views.about, name='about'),
    path('search/',views.Search,name='search'),
    path('search_auto/',views.search_auto,name='search_auto'),
    path('category/<int:id>/<slug:slug>', views.category_product, name='category_product'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('faq/', views.faq, name='faq'),

]
