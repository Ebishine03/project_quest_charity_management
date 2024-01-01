from django.urls import include, path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home),
    path('login/',views.login,name='login'),
    path('resetPass',views.reset,name='passRst'),
    path('register/',views.CreateUser)
]
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)