from django.urls import path
from base.views import order_views as views


urlpatterns = [
    path('add/', views.addOrderItem, name='orders-add' ),
    path('<str:pk>/', views.getOrderById, name='user-order' )

   
]
