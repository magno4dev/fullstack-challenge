from django.conf.urls import url
from django.urls import path, include
from .views import OrderApi

urlpatterns = [
    path('order', OrderApi.as_view()),
]