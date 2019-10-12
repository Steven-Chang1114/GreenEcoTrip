from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads
from .skyscanner_api_calls import LiveResults, place_autosuggest
from .google_api_calls import GMapsWrapper
from .utilities import calculate_flight_emission, TrainResultTransformer


# Create your views here.

@csrf_exempt
def result_view(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        data = loads(body_unicode)
        return JsonResponse(get_routes(data))


def get_routes(params):
    train_obj = GMapsWrapper('AIzaSyCUPvUnI4COqOfF73iRo32tRd8wQp_M4f8')
    train_origin = transform_place_flight_to_train(params, 'originPlace')
    train_destination = transform_place_flight_to_train(params, 'destinationPlace')

    train_results = train_obj.transit_routes_between(train_origin, train_destination, params['outboundDate'])
    train_results = TrainResultTransformer(list(r.filter_transit_steps()) for r in train_results).transform()

    flight_obj = LiveResults(params)
    flight_obj.poll_results()
    flight_results = flight_obj.filter_results()

    results = {
        'Trains': sorted(train_results, key=lambda x: x['Emissions']),
        'Planes': sorted(flight_results, key=lambda x: x['Emissions'])
    }

    return results


def transform_place_flight_to_train(params, station):
    clean_place_id = params[station].split('-')[0]
    place = place_autosuggest(params['country'], params['currency'], params['locale'], clean_place_id)
    return place[0]['PlaceName']


if __name__ == '__main__':
    country = 'UK'
    currency = 'EUR'
    locale = 'en-UK'

    origin = 'CDG-sky'
    destination = 'EDI-sky'
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
    print('einef')