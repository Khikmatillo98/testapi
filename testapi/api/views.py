from django.shortcuts import render
from .models import Poll, Choice , Vote
from .serializers import PollSerializer , ChoiceSerializer, VoteSerializer
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

class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer



class CreateVote(generics.CreateAPIView):
    query = Vote.objects.all()
    serializer_class = VoteSerializer  