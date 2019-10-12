from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def result_view(request):
    if request.method == "GET":
        pass


def get_routes(params):
    train_obj = GMapsWrapper('AIzaSyCUPvUnI4COqOfF73iRo32tRd8wQp_M4f8')
    train_origin = transform_place_flight_to_train(params, 'originPlace')
    train_destination = transform_place_flight_to_train(params, 'destinationPlace')

    train_results = train_obj.transit_routes_between(train_origin, train_destination, params['outboundDate'])
    train_results = TrainResultTransformer(list(r.filter_transit_steps()) for r in train_results).transform()

    flight_obj = LiveResults(params)
    flight_obj.poll_results()
    flight_results = flight_obj.filter_results()  # + flight_obj.filter_results(1)

    results = train_results + flight_results
    average_emissions = np.mean([x['Emissions'] for x in results])
    average_duration = np.mean([x['Duration'] for x in results])

    return sorted(results, key=lambda x: x['Emissions'])

def transform_place_flight_to_train(params, station):
    clean_place_id = params[station].split('-')[0]
    place = place_autosuggest(params['country'], params['currency'], params['locale'], clean_place_id)
    return place[0]['PlaceName']
