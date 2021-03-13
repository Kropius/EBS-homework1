import random
from data import CITIES, DIRECTIONS, \
    TOTAL_NR_OF_STATIONS, MAXIMUM_TEMPERATURE, MINIMUM_TEMPERATURE, \
    MINIMUM_WIND_SPEED, MAXIMUM_WIND_SPEED
from data import get_min_len_dataset as gmld
from datetime import date


def generate_cities(total_nr_of_items):
    return [CITIES[random.randint(0, len(CITIES) - 1)] for _ in range(total_nr_of_items)]


def generate_stations(total_nr_of_items):
    return [random.randint(0, TOTAL_NR_OF_STATIONS) for _ in range(total_nr_of_items)]


def generate_temperatures(total_nr_of_items):
    return [random.randint(MINIMUM_TEMPERATURE, MAXIMUM_TEMPERATURE) for _ in range(total_nr_of_items)]


def generate_rain_chance(total_nr_of_items):
    return [random.uniform(0, 1) for _ in range(total_nr_of_items)]


def generate_wind_speeds(total_nr_of_items):
    return [random.randint(MINIMUM_WIND_SPEED, MAXIMUM_WIND_SPEED) for _ in range(total_nr_of_items)]


def generate_directions(total_nr_of_items):
    return [random.choice(DIRECTIONS) for _ in range(total_nr_of_items)]


def generate_dates(total_nr_of_items):
    dates = []
    for _ in range(total_nr_of_items):
        start_date = date.today().replace(day=1, month=1).toordinal()
        end_date = date.today().toordinal()
        random_day = date.fromordinal(random.randint(start_date, end_date))
        dates.append(random_day.isoformat())
    return dates


def return_min_domain():
    return gmld()
