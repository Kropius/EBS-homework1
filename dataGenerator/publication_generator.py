import random
from data import CITIES,DIRECTIONS,TOTAL_NR_OF_PUBLICATIONS,\
    TOTAL_NR_OF_STATIONS,MAXIMUM_TEMPERATURE,MINIMUM_TEMPERATURE,\
    MINIMUM_WIND_SPEED,MAXIMUM_WIND_SPEED
from data import get_min_len_dataset as gmld
from datetime import date


def generate_cities():
    return [CITIES[random.randint(0,len(CITIES)-1)] for _ in range(TOTAL_NR_OF_PUBLICATIONS)]


def generate_stations():
    return [random.randint(0,TOTAL_NR_OF_STATIONS) for _ in range(TOTAL_NR_OF_PUBLICATIONS)]


def generate_temperatures():
    return [random.randint(MINIMUM_TEMPERATURE,MAXIMUM_TEMPERATURE) for _ in range(TOTAL_NR_OF_PUBLICATIONS)]


def generate_rain_chance():
    return[random.uniform(0,1) for _ in range(TOTAL_NR_OF_PUBLICATIONS)]


def generate_wind_speeds():
    return[random.randint(MINIMUM_WIND_SPEED,MAXIMUM_WIND_SPEED) for _ in range(TOTAL_NR_OF_PUBLICATIONS)]


def generate_directions():
    return [random.choice(DIRECTIONS) for _ in range(TOTAL_NR_OF_PUBLICATIONS)]


def generate_dates():
    dates = []
    for _ in range(TOTAL_NR_OF_PUBLICATIONS):
        start_date = date.today().replace(day=1, month=1).toordinal()
        end_date = date.today().toordinal()
        random_day = date.fromordinal(random.randint(start_date, end_date))
        dates.append(random_day.isoformat())
    return dates


def build_publications_dict():
    cities = generate_cities()
    stations = generate_stations()
    temperatures = generate_temperatures()
    rain_chances = generate_rain_chance()
    wind_speeds = generate_wind_speeds()
    directions = generate_directions()
    dates = generate_dates()

    return [build_publication(stations[i],cities[i],temperatures[i],
                              rain_chances[i],wind_speeds[i],directions[i],dates[i]) for i in range(TOTAL_NR_OF_PUBLICATIONS)]


def build_publication(stationId, city, temperature, rain_chance, wind_speed, direction, date):
    publication = {
        "stationId": stationId,
        "city": city,
        "temperature": temperature,
        "rainChangce": rain_chance,
        "windSpeed": wind_speed,
        "direction": direction,
        "date": date
    }
    return publication


print(build_publications_dict())

print(gmld())