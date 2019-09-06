import requests
import random
from django.conf import settings


API_HOST = "https://api.yelp.com/v3"
SEARCH_PATH = '/businesses/search'

def get_businesses(location, search_radius, offset):
    businesses = []
    search_radius *= 1609
    URL = API_HOST + SEARCH_PATH
    params = {
        'location': location,
        'limit': 50,
        'offset': offset,
        'open_now': True,
        'radius': search_radius,
        'categories': 'food,restaurants'
    }
    headers = {
        'Authorization' : 'Bearer %s' % settings.YELP_API_KEY,
    }
    #print(u'Querying {0} ...'.format(URL))
    response = requests.get(URL, headers=headers, params=params)
    #print('This is response status code: ')
    #print(response.status_code)
    return response.json()

# Creates a raw list of all the businesses and their relative information
def create_raw_business_list(location, radius):
    raw_businesses = []
    firstResponse = get_businesses(location, radius, 0)
    raw_businesses.extend(firstResponse['businesses'])
    totalBusinesses = firstResponse['total']
    offset = 50
    while (offset + 50) < totalBusinesses:
        nextResponse = get_businesses(location, radius, offset)
        raw_businesses.extend(nextResponse['businesses'])
        offset += 50
    return raw_businesses

# Chooses a business from the raw business list and return the name
def chooseRandomBusiness(raw_business_list, star_standard):
    totalBusinesses = len(raw_business_list)
    if (totalBusinesses == 0):
        print('Sorry! No businesses')
        return
    else:
        randomNum = random.randint(0, totalBusinesses)
        place_to_eat = raw_business_list[randomNum]
        # Generate new place to eat if it doesn't meet the standard
        while (place_to_eat['rating'] <= star_standard):
            randomNum = random.randint(0, totalBusinesses - 1)
            place_to_eat = raw_business_list[randomNum]
        return place_to_eat['name']
