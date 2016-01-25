import pyowm

from magic_mirror.keys import WEATHER_API_KEY


class OpenWeatherMapClient(object):
    def __init__(self):
        self.owm = pyowm.OWM(WEATHER_API_KEY)

    def get_weather(self):
        forecast = self.owm.weather_at_place("Ann Arbor, US")
        weather = forecast.get_weather()
        return weather.get_temperature('fahrenheit')

    # def __getattr__(self, method):
    #     return DeliciousClient(self.username, self.password, '%s/%s' % (self.method, method))

    def __repr__(self):
        return "<OpenWeatherMapClient>"
