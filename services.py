import requests


def request_name(name_search: str, world: bool) -> None:
    """

    :param name_search:
    :param world:
    :return:
    """
    response = requests.get(f"https://www.swapi.tech/api/people/?name={name_search}")
    response_text = response.json()

    if not response_text['result']:
        print("\nThe force is not strong within you\n")
        return

    print()
    for character in response_text['result']:
        print(f"Name: {character['properties']['name']}")
        print(f"Height: {character['properties']['height']}")
        print(f"Mass: {character['properties']['mass']}")
        print(f"Birth Year: {character['properties']['birth_year']}")
        print()
        if world:
            request_world(character['properties']['homeworld'])


def request_world(home_world: str) -> None:
    """

    :param home_world:
    :return:
    """
    response = requests.get(home_world)
    response_text = response.json()

    properties = response_text['result']['properties']

    print("Homeworld")
    print("---------")
    print(f"Name: {properties['name']}")
    print(f"Population: {properties['population']}")
    print()
    if properties['orbital_period'] != 'unknown' and properties['rotation_period'] != 'unknown':
        print(f"On {properties['name']}, 1 year on earth is {round(int(properties['orbital_period'])/365,2)} "
              f"years and 1 day {round(int(properties['rotation_period'])/24,2)} days")
    print()
