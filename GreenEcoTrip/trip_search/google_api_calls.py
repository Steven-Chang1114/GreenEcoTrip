'''
Google API calls exposes a class that wraps common use functions for the router
'''
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
        self.client.directions(
            start,
            terminal,
            mode='transit'
        )
