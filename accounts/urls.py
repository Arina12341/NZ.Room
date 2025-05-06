
from django.urls import path

from accounts.views import auth_page, register_form, logout_view

urlpatterns = [
    path('auth/', auth_page),
    path('register/', register_form),
    path('logout/', logout_view)
]