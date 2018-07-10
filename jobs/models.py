from django.db import models


class Job(models.Model):
    job_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255, null=False, blank=False)
    link = models.TextField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    webpage = models.CharField(max_length=255)
    company = models.CharField(max_length=255, null=True)