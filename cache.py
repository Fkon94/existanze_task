import atexit
import os
import pickle
from datetime import datetime

CACHE_FILE = os.path.join(os.getcwd(), 'cache.pkl')


def persist_to_file():
    try:
        with open(CACHE_FILE, 'rb') as handle:
            cache = pickle.load(handle)
    except (IOError, ValueError):
        cache = {}

    atexit.register(lambda: write_to_pickle(CACHE_FILE, cache))

    def decorator(func):
        def new_func(name, world):
            if (name, world) not in cache:
                # datetime object containing current date and time
                cache[(name, world)] = (func(name, world), datetime.now())
            return cache[(name, world)]

        return new_func

    return decorator


def clear_cache():
    if os.path.exists(CACHE_FILE):

        try:
            os.remove(CACHE_FILE)
        except OSError as e:  # name the Exception `e`
            print("Failed with:", e.strerror)  # look what it says

        print("removed cache")
    else:
        print("No cache found.")


def write_to_pickle(filename, cache):
    with open(filename, 'wb') as handle:
        pickle.dump(cache, handle, protocol=pickle.HIGHEST_PROTOCOL)
