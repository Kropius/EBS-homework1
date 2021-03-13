TOTAL_NR_OF_PUBLICATIONS = 20
TOTAL_NR_OF_SUBSCRIPTIONS = 20
TOTAL_NR_OF_STATIONS = 4

MAXIMUM_TEMPERATURE = 45
MINIMUM_TEMPERATURE = -45

MINIMUM_WIND_SPEED = 0
MAXIMUM_WIND_SPEED = 200

CITIES = ['ROMAN','IASI','CONSTANTA','BRAILA','COSTINESTI','PASCANI','GALATI','BACAU','VASLUI','BLAGESTI']
DIRECTIONS = ['S','SW','SE','NW','NE','N','E','W']

EQUALITY_FREQUENCY = 50


def get_min_len_dataset():
    minimum_domain_length = len(CITIES)
    minimum_domain_name = 'city'
    if len(DIRECTIONS) < minimum_domain_length:
        minimum_domain_length = len(DIRECTIONS)
        minimum_domain_name = 'direction'

    if(MAXIMUM_TEMPERATURE-MINIMUM_TEMPERATURE+1) < minimum_domain_length:
        minimum_domain_length = MAXIMUM_TEMPERATURE-MINIMUM_TEMPERATURE+1
        minimum_domain_name = 'temp'

    if(MAXIMUM_WIND_SPEED-MINIMUM_WIND_SPEED) < minimum_domain_length:
        minimum_domain_length = MAXIMUM_WIND_SPEED-MINIMUM_WIND_SPEED+1
        minimum_domain_name = 'wind'

    if TOTAL_NR_OF_STATIONS < minimum_domain_length:
        minimum_domain_name = 'stationId'

    return minimum_domain_name, EQUALITY_FREQUENCY
