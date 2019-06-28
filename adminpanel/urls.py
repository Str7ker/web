from django.urls import path, include
from adminpanel.views import *

urlpatterns = [
    path('panel/', dashboard, name='dashboard'),
    path('panel/<int:pk>/', dashboard_del, name='dashboard_del'),
    path('panel/page_index/', page_index, name='page_index'),
    path('panel/page_index/<int:pk>/', page_index_del, name='page_index_del'),
    path('panel/logo/', logo, name='logo'),
    path('panel/logo/<int:pk>/', logo_del, name='logo_del'),
    path('panel/gruz/', gruz, name='gruz'),
    path('panel/gruz/<int:pk>/', gruz_del, name='gruz_del'),
    path('panel/work/', work, name='work'),
    path('panel/work/<int:pk>/', work_del, name='work_del'),
    path('panel/part/', part, name='part'),
    path('panel/part/<int:pk>/', part_del, name='part_del'),
    path('panel/pred/', pred, name='pred'),
    path('panel/pred/<int:pk>/', pred_del, name='pred_del'),
    path('panel/team_index/', team_index, name='team_index'),
    path('panel/team_index/<int:pk>/', team_index_del, name='team_index_del'),
    path('panel/partners/', partners, name='partners'),
    path('panel/partners/<int:pk>/', partners_del, name='partners_del'),
    path('panel/teams/', teams, name='teams'),
    path('panel/teams/<int:pk>/', teams_del, name='teams_del'),

]
