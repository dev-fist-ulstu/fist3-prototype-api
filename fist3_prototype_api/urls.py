from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core.constants import ApiVersionPaths

urlpatterns = [
    path(ApiVersionPaths.API_V1, include("modules.user.urls")),
    path(ApiVersionPaths.API_V1, include("modules.document.urls")),
    path(ApiVersionPaths.API_V1, include("modules.admin.urls")),
    path(ApiVersionPaths.API_V1, include("modules.files.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
