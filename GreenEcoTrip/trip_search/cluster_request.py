from skyscanner_api_calls import LiveResults
from skyscanner_api_calls import place_autosuggest
import time


def get_flights_datas(cluster_d, cluster_a):
    # for every city in the departure cluster, send request to Skyscanner
    # return: the datas from skyskanner (used in binarymatrix.py)

    results = []

    for departure in cluster_d:
        for arrival in cluster_a:
            country = 'UK'
            currency = 'EUR'
            locale = 'en-UK'

            print("deparutre", departure)
            print("arrival", arrival)

            departure_date = '2019-12-03'
            return_date = '2019-12-10'

            params = {
                'country': country,
                'currency': currency,
                'locale': locale,
                'originPlace': departure['PlaceId'],
                'destinationPlace': arrival['PlaceId'],
                'outboundDate': departure_date,
                'inboundDate': return_date,
                'adults': 1
            }

            obj = LiveResults(params)
            obj.create_session()
            #obj.poll_results()
            results.append(obj.filter_results() + obj.filter_results(1))
            print("Ye")

    return results


if __name__ == '__main__':
    country = 'UK'
    currency = 'EUR'
    locale = 'en-UK'
    print(type(place_autosuggest(country, currency, locale, 'Paris')[0]))
    D = [place_autosuggest(country, currency, locale, 'Paris')[0],
         place_autosuggest(country, 'EUR', locale, 'Berlin')[0]]
    A = [place_autosuggest(country, currency, locale, 'Manchester')[0],
         place_autosuggest(country, 'EUR', locale, 'London')[0]]

    t = time.time()
    datas = get_flights_datas(D, A)

    print("yooooooooooo", time.time() - t)
    #print(datas)

    ids = []

    for i in datas:
        for dict in i:
            ids.append((dict['OutboundLegId']['Id'], dict['InboundLegId']['Id']))

    if len(ids) == len(set(ids)):
        print("no duplicates", len(ids), len(set(ids)))
    else:
        print("duplicates", len(ids), len(set(ids)))
