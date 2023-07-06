from rest_framework import serializers
import requests
from .models import Crawler

class CrawlerSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    def get_tags(self, instance):
        pass

    
    class Meta:
        model = Crawler
        fields = ('id', 'url', 'keyword', 'tags')