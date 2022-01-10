from typing import Union, Dict, Any
import requests
from flask import Blueprint

weather = Blueprint('weather', __name__)

apikey = 'zvyMhPJVn3PMtoDWjF4764GdQavSV3et'


def get_city_key(city_name: str, country_id: str) -> str:
    """
    Method retrieves city location code for search for forecast search on 3rd part API
    :param city_name: city name entered
    :param country_id: country name entered to identify specific cities with the same name in various countries
    :return: expected return city code or 'Not Found'
    """
    city_key_info = requests.get(
        'http://dataservice.accuweather.com/locations/v1/cities/search?apikey=' + apikey + '&q=' + city_name).json()
    try:
        for i in range(len(city_name)):
            if country_id == city_key_info[i]['Country']['ID']:
                return city_key_info[i]['Key']
    except IndexError:
        return 'Not Found'


@weather.route('/weather/<city_name>/<country_id>', methods=['GET'])
def weather_info(city_name: str, country_id: str) -> Union[Union[str, dict[str, Union[dict[str, Any], Any]]], Any]:
    """
    Method retrieves forecast of 1 day for specific city using location code
    :param city_name: city name entered
    :param country_id: country name entered to identify specific cities with the same name in various countries
    :return: expected to return city forecast or 'Not Found' varying on the error
    """
    try:
        city_weather_info = requests.get(
            'http://dataservice.accuweather.com/forecasts/v1/daily/1day/'
            + get_city_key(city_name, country_id.upper()) + '?apikey=' + apikey + '&metric=true').json()
    except TypeError:
        return 'Not found'
    try:
        return {
            'Date': city_weather_info['DailyForecasts'][0]['Date'],
            'Day': city_weather_info['DailyForecasts'][0]['Day']['IconPhrase'],
            'Night': city_weather_info['DailyForecasts'][0]['Night']['IconPhrase'],
            'Temperature': {
                'Min': city_weather_info['DailyForecasts'][0]['Temperature']['Minimum']['Value'],
                'Max': city_weather_info['DailyForecasts'][0]['Temperature']['Maximum']['Value']
            }
        }
    except KeyError:
        return city_weather_info['Message']



