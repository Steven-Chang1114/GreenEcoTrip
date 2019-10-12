import datetime

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
            itinerary['OutboundLegId'] = self.transform_leg(itinerary['OutboundLegId'])
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