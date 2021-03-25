from GenerateSubscriptions import GenerateSubscriptions
from GeneratePublications import GeneratePublications
from data import TOTAL_NR_OF_PUBLICATIONS, TOTAL_NR_OF_SUBSCRIPTIONS, SUBSCRIPTION_FIELD_FREQUENCIES


def main():

    publication_generator = GeneratePublications(TOTAL_NR_OF_PUBLICATIONS)
    publications = publication_generator.build_publications_dict()
    with open('publications.txt', 'w') as publication_fd:
        for elem in publications:
            publication_fd.write(str(elem))
            publication_fd.write('\n')

    subscription_generator = GenerateSubscriptions(TOTAL_NR_OF_SUBSCRIPTIONS, SUBSCRIPTION_FIELD_FREQUENCIES)
    subscriptions = subscription_generator.generate_subscriptions()
    with open('subscriptions.txt', 'w') as subscription_fd:
        for elem in subscriptions:
            subscription_fd.write(str(elem))
            subscription_fd.write('\n')


main()
