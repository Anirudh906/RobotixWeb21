from django.shortcuts import render
from .models import Event,Workshop
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EventSerializer, WorkshopSerializer


# Create your views here.

@api_view()
def event_api(request):
    obj_event = Event.objects.all()
    obj_work = Workshop.objects.all()
    serializer1 = EventSerializer(obj_event,many=True)
    serializer2 = WorkshopSerializer(obj_work,many=True)
    dict = {'Event':serializer1.data, 'Workshop':serializer2.data}

    return Response(dict)
