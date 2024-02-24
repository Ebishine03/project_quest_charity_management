

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [

    path('login/',views.user_login, name='login'),
    path('logout/',views.user_logout, name='logout'),
    # ... other URL patterns
]
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)