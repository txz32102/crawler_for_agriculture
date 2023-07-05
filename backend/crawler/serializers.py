from rest_framework import serializers
import requests
from .models import Crawler

class CrawlerSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    def get_tags(self, instance):
        url = instance.url
        keyword = instance.keyword

        # Make a request to the URL
        response = requests.get(url)
        content = response.text

        # Search for the keyword in the content
        if keyword in content:
            return content
        else:
            return "Keyword not found in the URL content."

    
    class Meta:
        model = Crawler
        fields = ('id', 'url', 'keyword', 'tags')