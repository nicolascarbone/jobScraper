from rest_framework import serializers

from jobs.models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('job_id', 'title', 'description', 'link', 'webpage')
