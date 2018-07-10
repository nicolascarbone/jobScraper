
from rest_framework.response import Response
from .serializers import JobSerializer
from jobs.models import Job
from rest_framework import viewsets


class ApiViewSet(viewsets.ModelViewSet):
    """
    Returns a list of all previous games.
    """
    serializer_class = JobSerializer
    queryset = Job.objects.all()

    # def get_queryset(sef):
    #     return Job.objects.all()

    # def list(self, request):
    #     scrawl.delay('gurudotcom')
    #     jobs = self.get_queryset()
    #     # jobs = Job.objects.all()
    #     serializer = self.get_serializer(jobs, many=True)
    #     return Response(serializer.data)
