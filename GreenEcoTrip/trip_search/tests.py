from django.test import TestCase
from skyscanner_api_calls import LiveResults, calculate_flight_emission
from google_api_calls import *

# Create your tests here.

def get_routes(params):
    obj = LiveResults(params)
    obj.poll_results()
    flight_results = obj.filter_results() + obj.filter_results(1)
    legs = ['OutboundLegId']

    if 'inboundDate' in params:
        legs.append('InboundLegId')

    for flight in flight_results:
        for leg in legs:
            flight[leg]['Emissions'] = calculate_flight_emission(flight[leg])

    print('ASS')





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
        'inboundDate': return_date,
        'adults': 1
    }

    get_routes(params)