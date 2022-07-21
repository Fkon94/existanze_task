from cache import clear_cache
from commands import search_clean_function
from services import request_name, print_info

if __name__ == '__main__':
    """
    Main function that retrieves the searched name
    and the world that it belongs, through Star Wars API.
    or
    Called to clear the cached data
    At the end it prints the result on console.
    """
    args = search_clean_function()
    if args.command == 'cache':
        clear_cache()
    elif args.command == 'search':
        characters_info, cache_time = request_name(args.name, args.world)
        print_info(characters_info)
        print(f'cached:{cache_time}')

