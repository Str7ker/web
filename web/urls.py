"""web URL Configuration

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
    1. Import the include() function: ........................` from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from web import settings
from django.contrib import admin
from django.urls import path, include
from index.views import *
from movizor.views import *
from partners.views import index_partners
from team.views import *
from company.views import *
from contact.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', index, name="index"),
    path('create/', mailss),
    path('movizor/', index_movizor, name="movizor"),
    path('partners/', index_partners, name="partners"),
    path('team/', index_team, name="team"),
    path('company/', index_company, name="index_company"),
    path('contact/', Contact.as_view(), name="contact"),
    path('', include('adminpanel.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()