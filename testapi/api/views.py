from django.shortcuts import render
from .models import Poll, Choice 
from .serializers import PollSerializer 
from django.http import JsonResponse 
from rest_framework.views import APIView 
from rest_framework.response import Response 
from django.shortcuts import get_object_or_404
from rest_framework import generics 

# Create your views here.

class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    # def get(self, request):
    #     polls = Poll.objects.all()[:20]
    #     data = PollSerializer(polls, many=True).data
    #     return Response(data)



class PollDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    # def get(self, request, pk):
    #     poll = get_object_or_404(Poll, pk=pk)
    #     data = PollSerializer(poll).data 
    #     return Response(data)