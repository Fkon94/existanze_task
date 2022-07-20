import argparse


def search_clean_function():
    """
    Function that defines the console parameters (search 'name' -- world) and (clean --cache)
    :return: the name that searched on command line (search 'Luke Sky'), the boolean parameter --world if provided
    or prints the message tha cache removed if cache parameter provided
    """
    parser = argparse.ArgumentParser(description='Search Star Wars Characters.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    subparsers = parser.add_subparsers()
    # Define the search parser as a subparser before name parameter
    search_parser = subparsers.add_parser('search')
    # Define the name parser that is a string after the search parameter
    search_parser.add_argument('name', type=str, help='Name to search')
    # Define the bool parameter --world after name parameter
    search_parser.add_argument('--world', action='store_true', help='Show world info')

    # Define the cache parser as a subparser before --clean parameter
    cache_parser = subparsers.add_parser('cache')
    # Define the bool parameter --clean after cache parameter
    cache_parser.add_argument('--clean', action='store_true', help='CLear cached data')

    # Parse command line's parameters
    args = parser.parse_args()
    if 'clean' in args:
        if args.clean:
            print("removed cache")
        else:
            print("Type cache --clean to clear the cache")
    else:
        return args.name, args.world


