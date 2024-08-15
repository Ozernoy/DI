'''
Using the requests and time modules, create a function which returns the amount of time it takes a webpage to load (how long it takes for a complete response to a request).
Test your code with multiple sites such as google, ynet, imdb, etc.
'''

import requests
import time

def measure_load_time(url: str) -> float:
    """Measure the time it takes for a webpage to load completely."""
    start_time = time.time()  
    requests.get(url)  
    end_time = time.time()  

    load_time = end_time - start_time

    return load_time

sites = [
    "https://www.google.com",
    "https://www.ynetnews.com",
    "https://www.imdb.com",
    "https://www.wikipedia.org"
]

for site in sites:
    load_time = measure_load_time(site)
    print(f"Time taken to load {site}: {load_time:.4f} seconds")
