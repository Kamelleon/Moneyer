"""Moneyer URL Configuration

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

from to_get_back_money.views import GetBackListView, GetBackCreateView, GetBackDetailView, GetBackDeleteView, GetBackUpdateView
from to_return_money.views import ReturnListView, ReturnCreateView, ReturnDetailView, ReturnDeleteView, ReturnUpdateView

urlpatterns = [
    path('', GetBackListView.as_view()),
    path('admin/', admin.site.urls),

    path('to_get_back/', GetBackListView.as_view(), name='to-get-back-list'),
    path('to_get_back/create', GetBackCreateView.as_view(), name='to-get-back-create'),
    path('to_get_back/<int:id>', GetBackDetailView.as_view(), name='to-get-back-details'),
    path('to_get_back/delete/<int:id>', GetBackDeleteView.as_view(), name='to-get-back-delete'),
    path('to_get_back/update/<int:pk>', GetBackUpdateView.as_view(), name='to-get-back-update'),

    path('to_return/', ReturnListView.as_view(), name='to-return-list'),
    path('to_return/create', ReturnCreateView.as_view(), name='to-return-create'),
    path('to_return/<int:id>', ReturnDetailView.as_view(), name='to-return-details'),
    path('to_return/delete/<int:id>', ReturnDeleteView.as_view(), name='to-return-delete'),
    path('to_return/update/<int:pk>', ReturnUpdateView.as_view(), name='to-return-update'),
]
