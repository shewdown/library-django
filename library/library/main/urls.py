from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.main, name='main'),
    path('catalog', views.catalog, name='catalog'),
    path('favorites', views.favorites, name='favorites'),
    path('news', views.news, name='news'),
    path('support', views.support, name='support'),
    path('reg', views.reg, name='reg'),
    path('log', views.log, name='log'),
    path('profile', views.profile, name='profile'),
    path('logout', views.full_logout, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)