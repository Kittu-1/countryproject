from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=30)

    def __str__(self):
        return self.country_name


class State(models.Model):
    state_name = models.CharField(max_length=30)
    country_name = models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.state_name


class City(models.Model):
    city_name = models.CharField(max_length=30)
    state_name = models.ForeignKey(State,on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name
