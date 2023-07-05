from django.urls import path
from . import views

app_name = 'Websell'
urlpatterns = [
    path('', views.indexClass.as_view(), name='index'),
    path('home/', views.HomeClass.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.products, name='products'),
    path('user/', views.User.as_view(), name='user'),
    path('handleuser/', views.HandleUser.as_view(), name='handleuser'),
    path('handlecontact/', views.Contact.as_view(), name='handlecontact')
]