from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('product/<int:pk>/', views.product_detail, name='product_detail')
]