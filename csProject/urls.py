"""csProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('get_calendar', views.get_calendar, name="get_calendar"),
    path('create_appointment', views.create_appointment, name="create_appointment"),
    path('profile', views.profile, name="profile"),
    path('cancel_appointment', views.cancel_appointment, name="cancel_appointment"),
    path('accept_appointment_request', views.accept_appointment_request, name="accept_appointment_request"),
    path('decline_appointment_request', views.cancel_appointment, name="decline_appointment_request"),

    # Django Auth
    path('accounts/', include('allauth.urls')),
    path('profile/sign_up', views.sign_up, name="sign_up"),
    path('profile/login', views.login_user, name="login_user"),
    path('profile/logout', views.logout_user, name="logout_user"),
]
