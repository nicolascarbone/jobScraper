import json

from rest_framework import viewsets
from rest_framework.response import Response
from jobs.models import Job

from api.tasks import scrawl


class ScraperViewSet(viewsets.ViewSet):

    def get_queryset(self):
        # fix this
        return Job.objects.none()

    def clean(self, requests):
        Job.objects.all().delete()

    def scrape(self, request):
        spider = request.GET.get('spider')
        if spider:
            scrawl.delay(spider)

        return Response('Task ran succesfully')
