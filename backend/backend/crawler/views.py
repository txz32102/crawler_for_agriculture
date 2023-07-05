from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CrawlerSerializer
from .models import Crawler

class CrawlerView(viewsets.ModelViewSet):
    serializer_class = CrawlerSerializer

    def get_queryset(self):
        queryset = Crawler.objects.all().order_by('-id')[:1]
        return queryset
