"""
URL configuration for mint_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dotenv import load_dotenv
from django_otp.admin import OTPAdminSite
from lab.views import api_root_view

# Load env variables
load_dotenv()
if os.getenv("OTP_BYPASS", "False").lower() == "true":
    # Use default admin without OTP for initial setup
    pass
else:
    admin.site.__class__ = OTPAdminSite


urlpatterns = [
    path('', api_root_view, name='api-root'),
    path(settings.ADMIN_URL, admin.site.urls),
    path(settings.API_URL, include('lab.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
