import requests
from utilities import ResultTransformer

def flight_search_cached(country, currency, locale, origin, destination, departure_date, return_date=None):
    url = "https://www.skyscanner.net/g/chiron/api/v1/flights/browse/browseroutes/v1.0/"
    params = '{}/{}/{}/{}/{}/{}/'.format(country, currency, locale, origin, destination, departure_date)
    if return_date:
        params += return_date + '?'
    routes = requests.get(url + params, headers={'api-key': 'skyscanner-hackupc2019'})

    if routes.status_code == 200:
        content = routes.json()

    return content


def place_autosuggest(country, currency, locale, query):
    url = "https://www.skyscanner.net/g/chiron/api/v1/places/autosuggest/v1.0/{}/{}/{}?query={}".format(
        country, currency, locale, query
    )
    places = requests.get(url, headers={'api-key': 'skyscanner-hackupc2019'})

    if places.status_code == 200:
        return places.json()


def get_route_average_emission(origin, destination):
    url = 'https://www.skyscanner.net/g/chiron/api/v1/eco/average-emissions?routes="{%s, %s}"' % (origin, destination)
    response = requests.get(url, headers={'api-key': 'skyscanner-hackupc2019'})

    if response.status_code == 200:
        emission = response.json()
        return emission


class LiveResults:
    def __init__(self, params=None):
        self.url = "https://www.skyscanner.net/g/chiron/api/v1/flights/search/pricing/v1.0"
        self.params = params
        self.headers = {
            "api-key": "skyscanner-hackupc2019",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
            "X-Forwarded-For": "147.83.201.96"
        }

    def create_session(self):
        print('Creating session')
        try:
            response = requests.post(url=self.url, headers=self.headers, json=self.params)
            self.response_key = response.json()['session_id']
            self.get_headers = {'api-key': 'skyscanner-hackupc2019', "Accept": "application/json"}
        except KeyError:
            self.create_session()

        return response

    def poll_results(self):
        response = self.create_session()
        print('Polling results')
        print(response.status_code)
        while True:
            if response.status_code == 201:
                url = "https://www.skyscanner.net/g/chiron/api/v1/flights/search/pricing/v1.0?session_id={}" \
                    .format(self.response_key)

                results = requests.get(url=url, headers=self.get_headers)
                print(results.json()['Status'])
                if results.json()['Status'] == 'UpdatesComplete':
                    return results.json()
            elif response.status_code == 429:
                print('There have been too many requests in the past minute. Retrying...')
                self.poll_results()
                break

    def filter_results(self, params={'sortType': 'price', 'sortOrder': 'asc'}):
        url = "https://www.skyscanner.net/g/chiron/api/v1/flights/search/pricing/v1.0?session_id={}" \
            .format(self.response_key)

        results = requests.get(url=url, headers=self.get_headers, params=params)
        return ResultTransformer(results.json()).transform_results()



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

    obj = LiveResults(params)
    obj.poll_results()
    results = obj.filter_results()
    # print(place_autosuggest(country, currency, locale, 'Paris'))
    # print(flight_search_cached(country, currency, locale, origin, destination, departure_date, return_date))
    print(get_route_average_emission(origin, destination))
