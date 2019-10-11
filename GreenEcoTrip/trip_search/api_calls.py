import requests

def flight_search_cached(country, currency, locale, departure_place, arrival_place, departure_date, return_date=None):
    url = "https://www.skyscanner.net/g/chiron/api/v1/flights/browse/browseroutes/v1.0/"
    params = '{}/{}/{}/{}/{}/{}/'.format(country, currency, locale, departure_place, arrival_place, departure_date)
    if return_date:
        params += return_date + '?'
    routes = requests.get(url + params, headers={'api-key': 'skyscanner-hackupc2019'})

    if routes.status_code == 200:
        pass