from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from flower_app.views import add, show, delete_flower

urlpatterns = [
    path('flowerbed/admin/', admin.site.urls),
    path('flowerbed/', add, name='index'),
    path('flowerbed/add/', add, name='add'),
    path('flowerbed/delete-flower/<int:flower_id>/', delete_flower, name='delete_flower'),
    path('flowerbed/show/', show, name='show'),
    path("flowerbed/__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
