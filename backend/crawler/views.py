from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CrawlerSerializer
from .models import Crawler

# Create your views here.

class CrawlerView(viewsets.ModelViewSet):
    serializer_class = CrawlerSerializer
    queryset = Crawler.objects.all()