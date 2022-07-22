import argparse


def search_clean_function():
    """
    Function that defines the console parameters (search 'name' -- world, clean --cache, history)
    :return: the name that searched on command line (search 'Luke Sky'),
             the boolean parameter --world if provided
             or prints the message tha cache removed if cache parameter provided
             or prints the searches made provided that the user has not cleaned their cache beforehand
    """
    parser = argparse.ArgumentParser(description='Search Star Wars Characters.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    subparsers = parser.add_subparsers(dest='command')
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

    # Define the history parser as a subparser
    subparsers.add_parser('history')

    # Parse command line's parameters
    args = parser.parse_args()

    return args


