from django.urls import path
from . import views

urlpatterns = [
    path('anasayfa/', views.index, name='index'),
    path('', views.logins, name='logins'),
    path('signup', views.sign, name='sign'),
    path('logout/', views.log_out, name='log_out'),
    path('keks/', views.keks, name='keks'),
    path('pirog/', views.pirog, name='pirog'),
    path('tort/', views.tort, name='tort'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path("search/", views.Search.as_view(), name='search'),
    path('update_item/', views.updateitem, name='update_item'),
]