from django.urls import path, include
from adminpanel.views import *

urlpatterns = [
    path('panel/', dashboard, name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls'))
]