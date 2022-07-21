from typing import Dict, List, Union
import requests
from star_wars import cache


@cache.persist_to_file()
def request_name(name_search: str, world: bool) -> List[Dict[str, Dict[str, str]]]:
    """
    Function that makes a request through Star Wars API in order to retrieve data
    for the name that searched.
    Also retrieves data for the world that the name belong to if the --world parameter
    passed as a parameter.
    :param name_search: The name next to search parameter (search 'Luke Sky')
    :param world: --world parameter
    :return: Prints the name provided and the world that it belongs if world parameter provided
    """

    # Takes the response through the Star Wars API request
    response = requests.get(f"https://www.swapi.tech/api/people/?name={name_search}")
    # Json parse the API response
    response_text = response.json()

    # Calls request world function if --world command line parameter exists
    if world:
        for character in response_text['result']:
            character['homeworld'] = request_world(character['properties']['homeworld'])

    return response_text['result']


def print_info(characters: List[Dict[str, Dict[str, Union[Dict[str, str], str]]]]) -> None:
    # If there is not a result through the API request
    if not characters:
        print("\nThe force is not strong within you\n")
        return

    print()
    # Iterate through the API results
    for character in characters:
        print(f"Name: {character['properties']['name']}")
        print(f"Height: {character['properties']['height']}")
        print(f"Mass: {character['properties']['mass']}")
        print(f"Birth Year: {character['properties']['birth_year']}")
        print()
        if 'homeworld' in character:
            home = character['homeworld']
            print("Homeworld")
            print("---------")
            # Prints world's name
            print(f"Name: {home['name']}")
            # Prints world's population
            print(f"Population: {home['population']}")
            print()
            # Prints the world's timeline if the orbital_period & rotation_period are known
            if home['orbital_period'] != 'unknown' \
                    and home['rotation_period'] != 'unknown':
                print(f"On {home['name']}, 1 year on earth is "
                      f"{round(int(home['orbital_period']) / 365, 2)} "
                      f"years and 1 day {round(int(home['rotation_period']) / 24, 2)} days")
            elif home['orbital_period'] == 'unknown' \
                    and home['rotation_period'] != 'unknown':
                print(f"On {home['name']}, 1 year on earth is unknown "
                      f"years and 1 day {round(int(home['rotation_period']) / 24, 2)} days")
            elif home['orbital_period'] != 'unknown' \
                    and home['rotation_period'] == 'unknown':
                print(f"On {home['name']}, 1 year on earth is "
                      f"{round(int(home['orbital_period']) / 365, 2)} "
                      f"years and 1 day is unknown days")
            else:
                print(f"On {home['name']}, 1 year on earth is "
                      f"unknown years and 1 day is unknown days")
            print()


def request_world(home_world: str) -> Dict[str, str]:
    """
    Function that requests and then print the world that belongs to the
    Star Wars character provided on request_name function
    :param home_world: request url parameter for the name_search parameter provided on request_name function
    :return: Prints the API response according to the url provided
    """
    # Takes the response through the Star Wars API request
    response = requests.get(home_world)
    # Json parse the API response
    response_text = response.json()

    # Set properties variable as the result of the API response
    properties = response_text['result']['properties']

    return properties
