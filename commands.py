import argparse


def search_function():
    """

    :return:
    """
    parser = argparse.ArgumentParser(description='Search Star Wars Characters.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    subparsers = parser.add_subparsers()
    search_parser = subparsers.add_parser('search')
    search_parser.add_argument('name', type=str, help='Name to search')
    search_parser.add_argument('--world', action='store_true', help='Show world info')

    args = parser.parse_args()
    return args.name, args.world
