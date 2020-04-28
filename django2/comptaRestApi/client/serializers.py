from rest_framework import serializers
from .models import Client, Rasp


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id',
                  'mnemo',
                  'raison',
                  'adresse1',
                  'adresse2',
                  'codeinsee')


class RaspSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rasp
        fields = ('date',
                  'timestamp',
                  'type',
                  'temperature',
                  'hygrometrie',
                  'pression')
