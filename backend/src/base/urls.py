"""defop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import (
    index,
    OptionsListView, OptionsDeleteView,
    OptionsCreateView, OptionsUpdateView
)


urlpatterns = [
    path('', index, name='home'),
    path('options', login_required(OptionsListView.as_view()), name='options-list'),
    path('options_create', login_required(OptionsCreateView.as_view()), name='options-create'),
    path('options_update/<pk>/', login_required(OptionsUpdateView.as_view()), name='options-update'),
    path('options_delete/<pk>/', login_required(OptionsDeleteView.as_view()), name='options-delete'),
]
