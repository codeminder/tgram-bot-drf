import random
from django.shortcuts import render
from .models import Advise
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from .serializers import AdviseSerializer, DateTimeSerializer


class CurrentDateTimeView(APIView):
    
    """
    View to get the current date and time.
    """
    
    def get(self, request, format=None):
        """
        Return the current date and time.
        """
        now = datetime.now()
        serializer = DateTimeSerializer({'current_datetime': now})
        return Response(serializer.data)

class RandomAdvisesView(APIView):
    
    """
    View to get random advises.
    """
    
    def get(self, request, format=None):
        """
        Return three random advises.
        """
        advises = Advise.objects.all()
        random_advises = random.sample(list(advises), min(len(advises), 3))
        serializer = AdviseSerializer(random_advises, many=True)
        return Response(serializer.data)
    
def index(request):
    
    """
    View to tittle page.
    """
    
    return render(request, 'bot_quiz/index.html')