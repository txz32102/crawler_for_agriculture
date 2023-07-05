from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CrawlerSerializer

class CrawlerView(APIView):
    def post(self, request):
        serializer = CrawlerSerializer(data=request.data)
        if serializer.is_valid():
            crawler = serializer.save()
            tags = crawler.crawl_and_get_tags()
            return Response({'tags': tags})
        else:
            return Response(serializer.errors, status=400)
