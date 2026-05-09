from .views import pre_home, home
from django.urls import path


urlpatterns = [
    path('', pre_home, name='pre_home'),
    path('home/', home, name='home')
]