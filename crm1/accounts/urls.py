from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('products/', views.products, name="products"),
    path('custumer/<str:id>', views.custumer, name="custumer"),
    path('create_order/<str:id>', views.createOrder, name="create_order"),
    path('update_order/<str:id>/<str:cid>', views.updateOrder, name="update_order"),
    path('delete_order/<str:id>/<str:cid>', views.deleteOrder, name="delete_order"),
]