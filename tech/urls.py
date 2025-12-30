from django.urls import path

from tech.views import tech_home

urlpatterns = [
    path('', tech_home, name='tech_home'),
]