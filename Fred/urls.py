from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls'))
]

if settings.DEBUG:
    # Debug Toolbar
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    
    # Silk Profiler (optional but recommended)
    urlpatterns += [
        path('silk/', include('silk.urls', namespace='silk')),
    ]
