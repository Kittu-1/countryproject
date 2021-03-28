from rest_framework import serializers
from countryapp.models import Country,State,City

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = '__all__'

    def to_representation(self, instance):
        repr = super(StateSerializer, self).to_representation(instance)
        repr['country_name'] = instance.country_name.country_name
        return repr

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'
    def to_representation(self, instance):
        repr = super(CitySerializer, self).to_representation(instance)
        repr['state_name'] = instance.state_name.state_name
        return repr

