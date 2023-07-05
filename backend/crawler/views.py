from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CrawlerSerializer
from .models import Crawler

from rest_framework.viewsets import ModelViewSet

class CrawlerView(ModelViewSet):
    queryset = Crawler.objects.all()
    serializer_class = CrawlerSerializer
