from django.shortcuts import render
from .models import Candidate
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import CandidateSerializers
from rest_framework.response import Response
import json
# Create your views here.


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all().order_by('-total_experience')
    serializer_class = CandidateSerializers
    permission_classes = [permissions.IsAuthenticated]



