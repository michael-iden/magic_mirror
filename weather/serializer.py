from models import Weather
from rest_framework import serializers


class WeatherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weather
        fields = ('url', 'username', 'email', 'groups')
