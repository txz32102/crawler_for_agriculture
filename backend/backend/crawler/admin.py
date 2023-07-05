from django.contrib import admin
from .models import Crawler

class CrawlerAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'keyword', 'tags')

# Register your models here.

admin.site.register(Crawler, CrawlerAdmin)
