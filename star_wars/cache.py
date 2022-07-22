import os
import pickle
from datetime import datetime

# define the name of cached data file
CACHE_FILE = os.path.join(os.getcwd(), '../cache.pkl')


def persist_to_file():
    """
    Function that used as decorator in order to cache data
    :return: cache data, function or decorator
    """
    # define cache variable that retrieves cache data from file
    cache = read_cache()

    def decorator(func):
        def new_func(name, world):
            if (name, world) not in cache:
                # datetime.now() is a datetime object containing current date and time
                cache[(name, world)] = (func(name, world), datetime.now())
                # write to cache file the retrieved data
                write_to_pickle(CACHE_FILE, cache)
            return cache[(name, world)]

        return new_func

    return decorator


def clear_cache() -> None:
    """
    Function that deletes the cache file and prints the appropriate message
    :return: Print the appropriate message
    """
    if os.path.exists(CACHE_FILE):
        try:
            os.remove(CACHE_FILE)
        except OSError as e:  # name the Exception `e`
            print("Failed with:", e.strerror)

        print("removed cache")
    else:
        print("No cache found.")


def write_to_pickle(filename, cache) -> None:
    """
    Function that creates a pickle file that is going to keep cached data
    :param filename: cached filename
    :param cache: data to be cached
    :return: nothing
    """
    with open(filename, 'wb') as handle:
        # write a pickle file to keep cached data
        pickle.dump(cache, handle, protocol=pickle.HIGHEST_PROTOCOL)


def read_cache():
    """
    Function that reads a pickle file and returns file's cached data
    :return: the cached data
    """
    try:
        with open(CACHE_FILE, 'rb') as handle:
            return pickle.load(handle)
    except (IOError, ValueError):
        return {}
