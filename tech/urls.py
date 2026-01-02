from django.urls import path

from tech.views import members_area, tech_home

urlpatterns = [
    path('', tech_home, name='tech_home'),
    path('members/', members_area, name='members_area'),
]