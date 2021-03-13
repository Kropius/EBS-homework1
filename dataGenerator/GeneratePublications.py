from data_generator import *


class GeneratePublications:

    def __init__(self, TOTAL_NR_OF_PUBLICATIONS):
        self.TOTAL_NR_OF_PUBLICATIONS = TOTAL_NR_OF_PUBLICATIONS

    def build_publication(self, stationId, city, temperature, rain_chance, wind_speed, direction, date):
        publication = {
            "stationId": stationId,
            "city": city,
            "temperature": temperature,
            "rainChance": rain_chance,
            "windSpeed": wind_speed,
            "direction": direction,
            "date": date
        }
        return publication

    def build_publications_dict(self):
        cities = generate_cities(self.TOTAL_NR_OF_PUBLICATIONS)
        stations = generate_stations(self.TOTAL_NR_OF_PUBLICATIONS)
        temperatures = generate_temperatures(self.TOTAL_NR_OF_PUBLICATIONS)
        rain_chances = generate_rain_chance(self.TOTAL_NR_OF_PUBLICATIONS)
        wind_speeds = generate_wind_speeds(self.TOTAL_NR_OF_PUBLICATIONS)
        directions = generate_directions(self.TOTAL_NR_OF_PUBLICATIONS)
        dates = generate_dates(self.TOTAL_NR_OF_PUBLICATIONS)

        return [self.build_publication(stations[i], cities[i], temperatures[i],
                                  rain_chances[i], wind_speeds[i], directions[i], dates[i]) for i in
                range(self.TOTAL_NR_OF_PUBLICATIONS)]

