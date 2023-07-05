import requests
from bs4 import BeautifulSoup
from django.db import models

class Crawler(models.Model):
    url = models.URLField()
    keyword = models.CharField(max_length=100)
    tags = models.TextField(blank=True)

    def crawl_and_get_tags(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        tags_with_content = []
        for tag in soup.find_all():
            if self.keyword in tag.get_text():
                tags_with_content.append(tag.get_text())
        return tags_with_content
