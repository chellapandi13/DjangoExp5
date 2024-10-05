"""
URL configuration for exp15 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.login_session_view, name='login_session'),         # URL for sessions
    path('cookies/', views.login_cookie_view, name='login_cookie'),    # URL for cookies
    path('session-success/', views.session_success_view, name='session_success'),
    path('cookie-success/', views.cookie_success_view, name='cookie_success'),
]
