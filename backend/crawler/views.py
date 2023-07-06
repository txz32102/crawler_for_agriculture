from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import CrawlerSerializer
from .models import Crawler
from .web_crawler import crawl_keywords

# Create your views here.

class CrawlerView(viewsets.ModelViewSet):
    serializer_class = CrawlerSerializer
    queryset = Crawler.objects.order_by('-id')[:1]  # Query the last record

    @action(detail=False, methods=['post'])
    def crawl(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        url = data['url']
        keyword = data['keyword']

        # Crawl the data and store the tags back into the 'tags' field of 'data'
        tags = crawl_keywords(url, keyword)
        data['tags'] = tags

        print(data)

        return Response(data)