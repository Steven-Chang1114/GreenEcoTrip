from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads
from .skyscanner_api_calls import LiveResults, place_autosuggest
from .google_api_calls import GMapsWrapper
from .utilities import calculate_flight_emission, TrainResultTransformer
import numpy as np
import datetime
import requests


# Create your views here.

@csrf_exempt
def result_view(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        data = loads(body_unicode)
        return JsonResponse(get_routes(data))


import random


def offset_view(request):
    if request.method == "GET":
        """""Dictionary containing data per kg given CO2 emissions"""
        co2_data = {
            'lamb': 39.2,  # 'CO2 per kg'
            'beef': 27.0,
            'cheese': 13.5,
            'mile': 2.25,
            'new clothes': 25,
        }
        emission = request.GET['emissions']
        element = random.choice(list(co2_data.keys()))
        quantity = emission / co2_data[element]
        return JsonResponse({'item': element, 'value': quantity})


def get_train_routes(params):
    train_obj = GMapsWrapper('AIzaSyCUPvUnI4COqOfF73iRo32tRd8wQp_M4f8')
    train_origin = params['originPlace']
    train_destination = params['destinationPlace']

    train_results = []
    for i in np.linspace(4, 20, 5):
        time = datetime.time(hour=int(i), minute=0, second=0).isoformat()
        train_result = train_obj.transit_routes_between(train_origin, train_destination, params['outboundDate'], time)
        train_result = TrainResultTransformer(list(r.filter_transit_steps()) for r in train_result).transform()
        train_results += train_result

    return train_results


def get_routes(params):
    train_results = get_train_routes(params)

    params['originPlace'] = get_airport_code(params, params['originPlace'])
    params['destinationPlace'] = get_airport_code(params, params['destinationPlace'])

    flight_obj = LiveResults(params)
    flight_obj.poll_results()
    flight_results = flight_obj.filter_results()

    train_emissions = [r['Emissions'] for r in train_results]
    planes_emissions = [r['Emissions'] for r in flight_results]

    max_emissions = np.max(planes_emissions)

    results = {
        'Trains': sorted(train_results, key=lambda x: x['Emissions']),
        'Planes': sorted(flight_results, key=lambda x: x['Emissions']),
        'max': max_emissions

    }

    return results


def get_airport_code(params, place_name):
    place = place_autosuggest(params['country'], params['currency'], params['locale'], place_name)
    return place[0]['PlaceId']


""""
def carbon_offset(emission):
    url = 'https://api.cloverly.com/2019-03-beta/purchases/carbon'
    headers = {'Content-type': 'application/json', 'Authorization': 'Bearer private_key:6352a4f5b8cf5a82'}
    data = '{"weight":{"value":%d,"units":"kg"}}' % (emission)
    r = requests.post(url, headers=headers, data=data)
    print(r.text)
"""

if __name__ == '__main__':
    country = 'UK'
    currency = 'EUR'
    locale = 'en-UK'

    origin = 'Paris'
    destination = 'Edinburgh'
    departure_date = '2019-12-03'
    return_date = '2019-12-10'

    params = {
        'country': country,
        'currency': currency,
        'locale': locale,
        'originPlace': origin,
        'destinationPlace': destination,
        'outboundDate': departure_date,
        'adults': 1
    }
    results = get_routes(params)

    carbon_offset(results['Planes'][0]['Emissions'])
