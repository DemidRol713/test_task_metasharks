from django.urls import path, include

from .api import CreateOrderView, ListOrderView

urlpatterns = [
    path('create_order/', CreateOrderView.as_view()),
    path('list_orders/', ListOrderView.as_view())
]