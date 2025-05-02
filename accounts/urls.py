
from django.urls import path

from accounts.views import auth_page

urlpatterns = [
    path('auth/', auth_page)
]