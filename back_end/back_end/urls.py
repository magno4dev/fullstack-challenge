"""back_end URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, re_path
from order.views import OrderApi, CategoryApi

urlpatterns = [
    
    path('admin/', admin.site.urls),

    re_path(r'^api/order/(?P<pk>[0-9]+)$', OrderApi.find, name='find'),
    re_path(r'^api/order/del/(?P<pk>[0-9]+)$', OrderApi.delete, name='delete'),
    re_path(r'^api/order/put/(?P<pk>[0-9]+)$', OrderApi.update, name='update'),
    re_path(r'^api/order/', OrderApi.post),
    re_path(r'^api/orders/', OrderApi.get, name='get'),
    re_path(r'^api/categories/', CategoryApi.get, name='get'),
    

]
