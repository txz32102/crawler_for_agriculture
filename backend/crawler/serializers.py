from rest_framework import serializers
from .models import Crawler

class CrawlerSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    def get_tags(self, instance):
        return "Hello, world!"
    
    class Meta:
        model = Crawler
        fields = ('id', 'url', 'keyword', 'tags')