from django.urls import include, path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup/',views.users_signup,name='signup')
    
]
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)