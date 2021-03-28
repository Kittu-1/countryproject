from django.shortcuts import render
from countryapp.models import Country,State,City
from countryapp.serializers import CountrySerializer,StateSerializer,CitySerializer
from rest_framework import generics

import django_filters.rest_framework

# Create your views here.


class CountryList(generics.ListCreateAPIView):
    def get_queryset(self):
        return Country.objects.all()

    def perform_create(self, serializer):
        serializer.save()
    serializer_class= CountrySerializer


class StateList(generics.ListCreateAPIView):
    def get_queryset(self):
        return State.objects.all()

    def perform_create(self, serializer):
        serializer.save()
    serializer_class= StateSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['country_name']


class CityList(generics.ListCreateAPIView):
    def get_queryset(self):
        return City.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    serializer_class = CitySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['state_name']

class CountryDetails(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return Country.objects.all()
    serializer_class = CountrySerializer

class StateDetails(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return State.objects.all()
    serializer_class = StateSerializer

class CityDetails(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        return City.objects.all()
    serializer_class = CitySerializer
