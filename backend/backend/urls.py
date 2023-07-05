from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from crawler.views import CrawlerView

router = routers.DefaultRouter()
router.register(r'crawler', CrawlerView, 'crawler')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
