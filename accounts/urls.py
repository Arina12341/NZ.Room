
from django.urls import path

from accounts.views import auth_page, register_form, logout_view, account_detail, upload_avatar
from django.conf.urls.static import static
from nz_room import settings

urlpatterns = [
    path('auth/', auth_page),
    path('register/', register_form),
    path('logout/', logout_view),
    path('detail/<int:pk>/', account_detail),
    path('upload-avatar/', upload_avatar, name='upload_avatar'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)