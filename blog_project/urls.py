"""blog_project URL Configuration

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
from pathlib import Path
from django.contrib import admin
from django.urls import path, re_path, include
from allauth.account.views import confirm_email

urlpatterns = [
    path('admin/', admin.site.urls),

    #Local urls
    path('', include('users.urls')),

    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),

    #Third party urls
    path('accounts/', include('allauth.urls')),  #This is used to call out confirm email
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r"^rest-auth/registration/account-confirm-email/(?P<key>[\s\d\w().+-_',:&]+)/$", confirm_email, name="account_confirm_email"),
]
