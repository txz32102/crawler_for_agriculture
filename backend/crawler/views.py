from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CrawlerSerializer
from .models import Crawler

# Create your views here.

class CrawlerView(viewsets.ModelViewSet):
    serializer_class = CrawlerSerializer
    queryset = Crawler.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        # Modify the tags field in each item of the response data
        for item in data:
            item['tags'] = 'Hello, world!'

        return Response(data)