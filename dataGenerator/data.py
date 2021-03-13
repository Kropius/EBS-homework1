TOTAL_NR_OF_PUBLICATIONS = 20
TOTAL_NR_OF_SUBSCRIPTIONS = 40
TOTAL_NR_OF_STATIONS = 100

MAXIMUM_TEMPERATURE = 3
MINIMUM_TEMPERATURE = -3

MINIMUM_WIND_SPEED = 0
MAXIMUM_WIND_SPEED = 200

CITIES = ['ROMAN', 'IASI', 'CONSTANTA', 'BRAILA', 'COSTINESTI', 'PASCANI', 'GALATI', 'BACAU', 'VASLUI', 'BLAGESTI',
          'SUCEAVA', 'FALTICENI', 'BUCURESTI', 'CLUJ-NAPOCA', 'PIATRA NEAMT', 'BICAZ', 'TARGU NEAMT', 'PASCANI',
          'TARGU FRUMOS', 'PODU ILOAEI', 'CURTEA DE ARGES', 'TIMISOARA', 'SATU MARE']
DIRECTIONS = ['S', 'SW', 'SE', 'NW', 'NE', 'N', 'E', 'W']

EQUALITY_FREQUENCY = 75

SUBSCRIPTION_FIELD_FREQUENCIES = {
    "stationId": 100,
    "city": 90,
    "temperature": 10,
    "wind_direction": 30,
    "wind_speed": 50
}


def get_min_len_dataset():
    minimum_domain_length = len(CITIES)
    minimum_domain_name = 'city'
    if len(DIRECTIONS) < minimum_domain_length:
        minimum_domain_length = len(DIRECTIONS)
        minimum_domain_name = 'wind_direction'

    if (MAXIMUM_TEMPERATURE - MINIMUM_TEMPERATURE + 1) < minimum_domain_length:
        minimum_domain_length = MAXIMUM_TEMPERATURE - MINIMUM_TEMPERATURE + 1
        minimum_domain_name = 'temperature'

    if (MAXIMUM_WIND_SPEED - MINIMUM_WIND_SPEED + 1) < minimum_domain_length:
        minimum_domain_length = MAXIMUM_WIND_SPEED - MINIMUM_WIND_SPEED + 1
        minimum_domain_name = 'wind_speed'

    if 365 < minimum_domain_length:
        minimum_domain_length = 365
        minimum_domain_name = 'date'

    if TOTAL_NR_OF_STATIONS < minimum_domain_length:
        minimum_domain_name = 'stationId'

    return minimum_domain_name, EQUALITY_FREQUENCY
