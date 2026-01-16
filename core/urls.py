
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),  # All auth endpoints are in accounts/urls.py
    path('api/conversation/', include('conversation.urls')),
]

# Serve media files in development
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add CORS headers if needed
if hasattr(settings, 'CORS_ORIGIN_ALLOW_ALL') and settings.CORS_ORIGIN_ALLOW_ALL:
    from corsheaders.views import CorsPostCsrfView
    urlpatterns += [
        path('cors/', CorsPostCsrfView.as_view())
    ]
