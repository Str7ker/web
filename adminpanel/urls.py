from django.urls import path, include
from adminpanel.views import *

urlpatterns = [
    path('panel/', dashboard, name='dashboard'),
    path('panel/page_index/', page_index, name='page_index'),
    path('panel/page_index/<pk>/', page_index_del, name='page_index_del'),
]