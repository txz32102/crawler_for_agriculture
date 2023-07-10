from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .serializers import CrawlerSerializer
from .models import Crawler
from .web_crawler import crawl_links
# from .web_crawler import crawl_keywords

# Create your views here.

class CrawlerView(viewsets.ModelViewSet):
    serializer_class = CrawlerSerializer
    # queryset = Crawler.objects.all()
    queryset = Crawler.objects.order_by('-id')[:1]  # Query the last record

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data[0]
        print("list is being called")
        url = data['url']
        keyword = data['keyword']

        # Crawl the data and store the tags back into the 'tags' field of 'data'
        tags = crawl_links(url, keyword)
        data['tags'] = tags
        print(tags)
        return Response(data)
    
    def create(self, request, *args, **kwargs):
        data = request.data
        print(data)
        
        url = data['url']
        keyword = data['keyword']

        # Crawl the data and store the tags back into the 'tags' field of 'data'
        tags = crawl_links(url, keyword)
        if isinstance(tags, str):
            # If crawl_links returns an error message, set 'tags' to None
            data['tags'] = None
            return Response({'error': tags}, status=status.HTTP_400_BAD_REQUEST)
        else:
            data['tags'] = tags

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(data, status=status.HTTP_201_CREATED)