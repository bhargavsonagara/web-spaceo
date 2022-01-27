from django.urls import path
from . import views
urlpatterns = [
    path('', views.show, name='show'),
    path('index/', views.index, name='index'),
    path('account/', views.account, name='account'),
    path('cart/', views.cart, name='cart'),
    path('cart1/', views.cart1, name='cart1'),
    path('contact/', views.contact, name='contact'),
    path('product1/', views.product1, name='product1'),
    path('products/', views.products, name='products'),
    path('signup/', views.signup, name='signup'),
    path('follower/', views.follower, name='follower'),
]
