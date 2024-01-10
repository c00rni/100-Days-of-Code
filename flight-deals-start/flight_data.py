class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self, departure_city_name, departure_iata_code, destination_city_name, destination_iata_code, accepted_price) -> None:
        self.departure_city = departure_city_name
        self.departure_code = departure_iata_code
        self.destination_city_name = destination_city_name
        self.destination_code = destination_iata_code
        self.highiest_price_allowed = accepted_price
    