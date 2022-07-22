# Existanze Task

On this task we make a request to 'The Star Wars API' (https://www.swapi.tech/) 
in order to allow the user of the program to search based on the name of any character.

star_wars\commands.py file creates the accepted command line arguments in order to:
- search a name with or without world parameter like:
  - python main.py search 'luke sky' or python main.py search 'luke sky' --world
- cache clear like:
  - python main.py cache -- clean
- Provides a visualization with python main.py history command, which includes 
  - The searches made 
  - The result
  - Time of the search

star_wars\services.py file has:
- the functions tha make the requests in API (request_name() & request_world())
- the function that prints the searched result

star_wars\cache.py file has:
- persist_to_file() function that creates the decorator that caches data
- write_to_pickle() function that creates and writes data on a pickle file
- read_cache() function that reads and returns cached data from pickle file if exists
- clear_cache() function that deletes the cached data file

main.py file call all of the above depends on the argument provided on command line

requirements.txt has the necessary packages this project needs

