from commands import search_clean_function
from services import request_name

if __name__ == '__main__':
    """
    Main function that retrieves the searched name
    and the world that it belongs, through Star Wars API.
    or
    Called to clear the cached data
    At the end it prints the result on console.
    """
    if search_clean_function() is not None:
        name, world = search_clean_function()
        request_name(name, world)
