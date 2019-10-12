'''
Google API calls exposes a class that wraps common use functions for the router
'''
from functools import reduce
import googlemaps
import datetime


def calculate_seconds_from_date(departure_date):
    departure_date = datetime.datetime.strptime(departure_date, '%Y-%m-%d').date()
    base_date = datetime.date(year=1970, month=1, day=1)
    return (departure_date - base_date).total_seconds()


class GMapsWrapper:
    '''
    Wrapper class for gmaps functions needed by the router
    '''

    def __init__(self, api_key):
        self.client = googlemaps.Client(api_key)

    def nearby_airports(self, location, radius=1000):
        '''
        nearby_airports gets the airports nearby the given city within a radius R
        '''
        place = self.client.geocode(location)[0]['geometry']['location']
        airports = self.client.places_nearby(
            location=place,
            radius=radius,
            type='airport'
        )
        return airports

    def transit_routes_between(self, start, terminal, departure_date=datetime.date.today().isoformat()):
        '''
        transit_routes_between gets the alternative transport options between start and terminal
        '''
        params = {
            'mode': 'transit',
            'alternatives': True,
        }

        departure_time = calculate_seconds_from_date(departure_date)

        return list(map(Directions, self.client.directions(
            start,
            terminal,
            mode='transit',
            alternatives=True,
            departure_time=departure_time,
        )))


class Directions:
    '''
    Contains methods for parsing GMaps directions response
    '''

    # kg of CO_2 per person per meter
    footprint_table = {
        "METRO_RAIL": 0.032 / 1000,
        "HEAVY_RAIL": 0.032 / 1000,
        "COMMUTER_TRAIN": 0.032 / 1000,
        "HIGH_SPEED_TRAIN": 0.032 / 1000,
        "LONG_DISTANCE_TRAIN": 0.032 / 1000,
        "BUS": 0.070 / 1000,
    }

    def __init__(self, directions):
        self.path = directions

    def calculate_carbon_footprint(self):
        '''
        Sums the carbon footprint of transit steps
        '''
        co_two = 0
        for leg in self.path['legs']:
            for step in leg['steps']:
                transit_details = step.get('transit_details', {})
                line = transit_details.get('line', {})
                vehicle = line.get('vehicle')
                if vehicle is None:
                    continue
                co_two += self.footprint_table.get(vehicle['type'], 0) * step['distance']['value']

        return co_two

    def distance(self):
        '''
        Returns the distance of the entire route
        '''
        return reduce(lambda acc, x: acc + x['distance']['value'], self.path['legs'], 0)

    def filter_transit_steps(self):
        '''
        Gives transit steps
        '''
        for leg in self.path['legs']:
            for step in leg['steps']:
                if step.get('travel_mode') == 'TRANSIT':
                    yield {
                        'distance': step['distance'],
                        'duration': step['duration'],
                        'transit_detail': step['transit_details'],
                        'emissions': self.calculate_carbon_footprint()
                    }


if __name__ == '__main__':
    import json

    a = GMapsWrapper('AIzaSyCUPvUnI4COqOfF73iRo32tRd8wQp_M4f8')
    s = a.transit_routes_between('Princes Street', 'London')[0]
    nearby = a.nearby_airports('Edinburgh Airport', radius=100000)
    print("MY ASS IN YOUR FACE")
