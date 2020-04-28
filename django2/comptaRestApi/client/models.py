from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Client(models.Model):
    id = models.BigAutoField(primary_key=True)
    raison = models.CharField(max_length=255, blank=True, null=True)
    mnemo = models.CharField(max_length=255, blank=True, null=True)
    adresse1 = models.CharField(max_length=255, blank=True, null=True)
    adresse2 = models.CharField(max_length=255, blank=True, null=True)
    codeinsee = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client'


class Rasp(models.Model):
    date = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.CharField(primary_key=True, max_length=255)
    type = models.CharField(max_length=255, blank=True, null=True)
    temperature = models.CharField(max_length=255, blank=True, null=True)
    hygrometrie = models.CharField(max_length=255, blank=True, null=True)
    pression = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rasp'
