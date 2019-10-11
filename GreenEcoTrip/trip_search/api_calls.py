import requests


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
        self.url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/v1.0"
        self.params = params
        self.headers = {
            "api-key": "skyscanner-hackupc2019",
            "Content-Type": "application/x-www-form-urlencoded"
        }

    def create_session(self):
        print('Creating session')
        try:
            response = requests.post(url=self.url, headers=self.headers, data=self.params)
            self.response_key = response.headers['Location'].split('/')[-1]
            self.get_headers = {**{key: value for (key, value) in self.headers.items() if key != 'Content-Type'},
                                **{'Prefer': 'wait=120'}}
        except KeyError:
            self.create_session()

        return response

    def poll_results(self):
        response = self.create_session()
        print('Polling results')
        print(response.status_code)
        while True:
            if response.status_code == 201:
                url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/uk2/v1.0/{}" \
                      "?pageIndex=0".format(self.response_key)
                results = requests.get(url=url, headers=self.get_headers).json()
                print(results['Status'])
                if results['Status'] == 'UpdatesComplete':
                    break
            elif response.status_code == 429:
                print('There have been too many requests in the past minute. Retrying...')
                self.poll_results()
                break

if __name__ == '__main__':
    country = 'UK'
    currency = 'EUR'
    locale = 'en-UK'

    origin = 'CDG'
    destination = 'EDI'
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
        'adults':1
    }
    obj = LiveResults(params)
    obj.poll_results()
    # print(place_autosuggest(country, currency, locale, 'Paris'))
    # print(flight_search_cached(country, currency, locale, origin, destination, departure_date, return_date))
    print(get_route_average_emission(origin, destination))
