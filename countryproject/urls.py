"""countryproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from countryapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("country/",views.CountryList.as_view()),
    path("state/", views.StateList.as_view()),
    path("city/", views.CityList.as_view()),
    path("countrydetails/<int:pk>/",views.CountryDetails.as_view()),
    path("statedetails/<int:pk>", views.StateDetails.as_view()),
    path("citydetails/<int:pk>", views.CityDetails.as_view()),
]
