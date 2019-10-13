import datetime
import numpy as np


class ResultTransformer():
    def __init__(self, results):
        self.query = results['Query']
        self.itineraries = results['Itineraries']
        self.legs = results['Legs']
        self.segments = results['Segments']
        self.carriers = results['Carriers']
        self.agents = results['Agents']
        self.places = results['Places']
        self.currencies = results['Currencies']

    def transform_results(self):
        results = []
        for itinerary in self.itineraries:
            i = 0
            itinerary['Type'] = 'Flight'
            itinerary['OutboundLegId'] = self.transform_leg(itinerary['OutboundLegId'])
            itinerary['Emissions'] = calculate_flight_emission(itinerary['OutboundLegId'])
            itinerary['Duration'] = itinerary['OutboundLegId']['Duration']
            if 'InboundLegId' in itinerary:
                itinerary['InboundLegId'] = self.transform_leg(itinerary['InboundLegId'])

            prices = []
            for price in itinerary['PricingOptions']:
                agents = []
                for agent in price['Agents']:
                    agents.append(self.transform_agent(agent))
                price['Agents'] = agents
                prices.append(price)
            itinerary['PricingOptions'] = prices

            itinerary['Currency'] = self.currencies[0]
            if i == 0:
                itinerary['Places'] = self.places
            results.append(itinerary)
            i += 1
        return results

    def transform_leg(self, leg_id):
        for leg in self.legs:
            if leg['Id'] == leg_id:
                l = leg.copy()

        l['OriginStation'] = self.transform_place(l['OriginStation'])
        l['DestinationStation'] = self.transform_place(l['DestinationStation'])
        places = [l['OriginStation'], l['DestinationStation']]

        stops = []
        for stop in l['Stops']:
            stops.append(self.transform_place(stop))
        l['Stops'] = stops
        places += stops

        carriers = []
        for carrier in l['Carriers']:
            carriers.append(self.transform_carrier(carrier))
        l['Carriers'] = carriers.copy()

        if l['OperatingCarriers'] == l['Carriers']:
            operating_carriers = carriers.copy()
        else:
            operating_carriers = []
            for op_carrier in l['OperatingCarriers']:
                operating_carriers.append(self.transform_carrier(op_carrier))

        l['OperatingCarriers'] = operating_carriers.copy()

        for flight in l['FlightNumbers']:
            try:
                flight['CarrierId'] = self.transform_carrier(flight['CarrierId'], operating_carriers).copy()
            except LookupError:
                flight['CarrierId'] = self.transform_carrier(flight['CarrierId'], carriers).copy()

        if 'SegmentIds' in l:
            segments = []
            for segment in l['SegmentIds']:
                segments.append(self.transform_segment(segment, places, carriers, operating_carriers))
            connection_times = []
            for i in range(len(segments) - 1):
                arrival_time = datetime.datetime.fromisoformat(segments[i]['ArrivalDateTime'])
                departure_time = datetime.datetime.fromisoformat(segments[i + 1]['DepartureDateTime'])
                connection = str(departure_time - arrival_time)
                connection_times.append(connection)
            segments.append(connection_times)
            l['SegmentIds'] = segments

        return l

    def transform_segment(self, segment_id, places, carriers, operating_carriers):
        segment = self.segments[segment_id].copy()

        segment['OriginStation'] = self.transform_place(segment['OriginStation'], places)
        segment['DestinationStation'] = self.transform_place(segment['DestinationStation'], places)

        segment['Carrier'] = self.transform_carrier(segment['Carrier'], carriers)
        segment['OperatingCarrier'] = self.transform_carrier(segment['OperatingCarrier'], operating_carriers)

        return segment

    def transform_place(self, place_id, places=None):
        if places:
            for place in places:
                if place['Id'] == place_id:
                    return place
        else:
            for place in self.places:
                if place['Id'] == place_id:
                    return place
        raise LookupError

    def transform_carrier(self, carrier_id, carriers=None):
        if carriers:
            for carrier in carriers:
                if carrier['Id'] == carrier_id or isinstance(carrier_id, dict):
                    return carrier
        else:
            for carrier in self.carriers:
                if carrier['Id'] == carrier_id:
                    return carrier
        raise LookupError

    def transform_agent(self, agent_id):
        for agent in self.agents:
            if agent['Id'] == agent_id:
                return agent
        raise LookupError


class TrainResultTransformer():
    def __init__(self, results):
        self.results = results

    def transform(self):
        clean_results = []
        for r in self.results:
            clean_r = {'Details': self.transform_details(r),
                       'Distance': sum([d['distance']['value'] for d in r]) / 1000,
                       'Duration': np.round(sum([d['duration']['value'] for d in r]) / 60),
                       'Emissions': sum([d['emissions'] for d in r]),
                       'Type': 'Transit'
                       }
            clean_results.append(clean_r)

        return clean_results

    def transform_details(self, result):
        for r in result:
            r['transit_detail']['arrival_time']['value'] = calculate_date_from_seconds(
                r['transit_detail']['arrival_time']['value'])
            r['transit_detail']['departure_time']['value'] = calculate_date_from_seconds(
                r['transit_detail']['departure_time']['value'])
        return result


def calculate_date_from_seconds(date_in_seconds):
    base_date = datetime.date(year=1970, month=1, day=1)
    date = base_date + datetime.timedelta(seconds=date_in_seconds)
    return date.isoformat()


def calculate_flight_emission(leg):
    duration = 0
    for seg in leg['SegmentIds'][:-1]:
        duration += seg['Duration']

    hours = duration / 60
    return hours * 90 * (2/0.8)
