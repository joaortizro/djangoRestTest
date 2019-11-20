from .models import Problem
from rest_framework import generics
from .serializers import ProblemSerializer


class ProblemList(generics.ListCreateAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
