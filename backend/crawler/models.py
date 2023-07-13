from django.db import models

class Crawler(models.Model):
    url = models.URLField()
    keyword = models.CharField(max_length=100)
    tags = models.TextField(blank=True)


