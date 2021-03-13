import random
from data import CITIES,DIRECTIONS, \
    TOTAL_NR_OF_STATIONS,MAXIMUM_TEMPERATURE,MINIMUM_TEMPERATURE,\
    MINIMUM_WIND_SPEED,MAXIMUM_WIND_SPEED
from data import get_min_len_dataset as gmld
from datetime import date


def generate_cities(TOTAL_NR_OF_ITEMS):
    return [CITIES[random.randint(0,len(CITIES)-1)] for _ in range(TOTAL_NR_OF_ITEMS)]


def generate_stations(TOTAL_NR_OF_ITEMS):
    return [random.randint(0,TOTAL_NR_OF_STATIONS) for _ in range(TOTAL_NR_OF_ITEMS)]


def generate_temperatures(TOTAL_NR_OF_ITEMS):
    return [random.randint(MINIMUM_TEMPERATURE,MAXIMUM_TEMPERATURE) for _ in range(TOTAL_NR_OF_ITEMS)]


def generate_rain_chance(TOTAL_NR_OF_ITEMS):
    return[random.uniform(0,1) for _ in range(TOTAL_NR_OF_ITEMS)]


def generate_wind_speeds(TOTAL_NR_OF_ITEMS):
    return[random.randint(MINIMUM_WIND_SPEED,MAXIMUM_WIND_SPEED) for _ in range(TOTAL_NR_OF_ITEMS)]


def generate_directions(TOTAL_NR_OF_ITEMS):
    return [random.choice(DIRECTIONS) for _ in range(TOTAL_NR_OF_ITEMS)]


def generate_dates(TOTAL_NR_OF_ITEMS):
    dates = []
    for _ in range(TOTAL_NR_OF_ITEMS):
        start_date = date.today().replace(day=1, month=1).toordinal()
        end_date = date.today().toordinal()
        random_day = date.fromordinal(random.randint(start_date, end_date))
        dates.append(random_day.isoformat())
    return dates


def return_min_domain():
    return gmld()
