from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import Client, Rasp
from .serializers import ClientSerializer
from .serializers import RaspSerializer

@csrf_exempt
def client_list(request):
    if request.method == 'GET':
        client = Client.objects.all()
        client_serializer = ClientSerializer(client, many=True)
        return JsonResponse(client_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        client_data = JSONParser().parse(request)
        client_serializer = ClientSerializer(data=client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse(client_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def client_detail(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        client_serializer = ClientSerializer(client)
        return JsonResponse(client_serializer.data)

    elif request.method == 'PUT':
        client_data = JSONParser().parse(request)
        client_serializer = ClientSerializer(client, data=client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse(client_serializer.data)
        return JsonResponse(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        client.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def rasp_list(request):
    if request.method == 'GET':
        raspberry = Rasp.objects.all()
        rasp_serializer = RaspSerializer(raspberry, many=True)
        return JsonResponse(rasp_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        rasp_data = JSONParser().parse(request)
        rasp_serializer = RaspSerializer(data=rasp_data)
        if rasp_serializer.is_valid():
            rasp_serializer.save()
            return JsonResponse(rasp_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(rasp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def rasp_detail(request, pk):
    try:
        rapsberry = Rasp.objects.get(pk=pk)
    except Rasp.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        rasp_serializer = RaspSerializer(rapsberry)
        return JsonResponse(rasp_serializer.data)

    elif request.method == 'PUT':
        rasp_data = JSONParser().parse(request)
        rasp_serializer = RaspSerializer(rapsberry, data=rasp_data)
        if rasp_serializer.is_valid():
            rasp_serializer.save()
            return JsonResponse(rasp_serializer.data)
        return JsonResponse(rasp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        rapsberry.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
