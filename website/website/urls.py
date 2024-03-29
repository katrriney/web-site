from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hospital.urls')),
    path('zapis/', include('bd.urls')),
    path('users/', include('users.urls', namespace="users")),
] + static(settings.STATIC_URL, document_root=settings. STATIC_ROOT)

