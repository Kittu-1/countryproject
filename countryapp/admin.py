from django.contrib import admin
from countryapp.models import Country, State, City


admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)