from GenerateSubscriptions import GenerateSubscriptions


def main():
    total_number_of_subscriptions = 10
    field_frequencies = {
        "city": 90,
        "temp": 10,
        "wind_direction": 30
    }
    generator = GenerateSubscriptions(total_number_of_subscriptions, field_frequencies)
    generator.generate_subscriptions()


main()
