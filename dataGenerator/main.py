from GenerateSubscriptions import GenerateSubscriptions
from GeneratePublications import GeneratePublications
from data import TOTAL_NR_OF_PUBLICATIONS, TOTAL_NR_OF_SUBSCRIPTIONS


def main():

    publication_generator = GeneratePublications(TOTAL_NR_OF_PUBLICATIONS)
    publications = publication_generator.build_publications_dict()
    for elem in publications:
        print(elem)

    print()

    field_frequencies = {
        "city": 90,
        "temp": 10,
        "direction": 30
    }
    generator = GenerateSubscriptions(TOTAL_NR_OF_SUBSCRIPTIONS, field_frequencies)
    generator.generate_subscriptions()


main()
