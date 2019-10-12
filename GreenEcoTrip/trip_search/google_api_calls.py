'''
Google API calls exposes a class that wraps common use functions for the router
'''
from functools import reduce
import googlemaps

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
        airports = self.client.places(
            '',
            location=location,
            radius=radius,
            type='airport'
        )
        return airports

    def transit_routes_between(self, start, terminal):
        '''
        transit_routes_between gets the alternative transport options between start and terminal
        '''
        return map(Directions, self.client.directions(
            start,
            terminal,
            mode='transit'
        ))

class Directions:
    '''
    Contains methods for parsing GMaps directions response
    '''
    def __init__(self, directions):
        self.directions = directions

    def calculate_carbon_footprint(self):
        '''
        Sums the carbon footprint of transit steps
        '''
        return self.directions

    def distance(self):
        '''
        Returns the distance of the entire route
        '''
        return reduce(lambda acc, x: acc + x['distance']['value'], self.directions['legs'], 0)

'''
if __name__ == '__main__':
    import json
    a = GMapsWrapper('AIzaSyCUPvUnI4COqOfF73iRo32tRd8wQp_M4f8')
    s = a.transit_routes_between('Princes Street', 'London')
    print(json.dumps(s))
'''
