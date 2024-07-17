#!/usr/bin/env python3
'''A module with tools for request caching and tracking.
'''
import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()
'''The module-level Redis instance.
'''


def data_cacher(method: Callable) -> Callable:
    '''Caches the output of fetched data.
    '''
    @wraps(method)
    def invoker(url) -> str:
        '''The wrapper function for caching the output.
        '''
        # Increment the count for the URL
        redis_store.incr(f'count:{url}')
        
        # Check if the result is in the cache
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        
        # Fetch the result and cache it
        result = method(url)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    '''Returns the content of a URL after caching the request's response,
    and tracking the request.
    '''
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return ""

if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.example.com"
    
    # First access: Fetches from the URL and caches it
    print(get_page(url))
    
    # Second access within 10 seconds: Should return cached content
    time.sleep(5)
    print(get_page(url))
    
    # Third access after 10 seconds: Should fetch again as cache expired
    time.sleep(6)
    print(get_page(url))
    
    # Print access count
    print(f"Access count for {url}: {redis_store.get(f'count:{url}').decode('utf-8')}")
