from star_wars.cache import clear_cache, read_cache
from star_wars.commands import search_clean_function
from star_wars.services import request_name, print_info

if __name__ == '__main__':
    """
    Main function that retrieves the searched name
    and the world that it belongs (if requested), through Star Wars API, 
    with search 'name' --world command
    or
    Called to clear the cached data with cache --clean command
    or 
    Called to see the History of searches made, 
    the time made and the searched result 
    
    At the end it prints the result on console.
    """
    args = search_clean_function()
    if args.command == 'cache' and args.clean:
        clear_cache()
    elif args.command == 'search':
        characters_info, cache_time = request_name(args.name, args.world)
        print_info(characters_info)
        print(f'cached: {cache_time}')
    elif args.command == 'history':
        history_cache = read_cache()
        for search, result in history_cache.items():
            print(f"The search name is: {search[0]}, {'with' if search[1] else 'without'} world")
            print_info(result[0])
            print(f'Time of search: {result[1]}\n------------------------------------------')


