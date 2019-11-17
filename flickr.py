from random import seed
from random import randint
from datetime import datetime
from config import *

import logging
import requests

# Seed random number generator
seed(datetime.now())

# Enable logging 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


# Flickr search parameters
resultsPerPage = 250
size ="b"

# Return a random photo URL and the associated author URL
def get_image():
    response = requests.get(get_flickr_search_request_url())
    if response.status_code != 200:
        # Something went wrong
        print("Something went wrong.")
        return
    
    # generate a pseudorandom number
    rand = randint(0, resultsPerPage-1)

    # pick a photo
    photo = response.json()["photos"]["photo"][rand]

    # generate photoURL
    photoURL = make_photo_URL(photo.get("farm"), 
        photo.get("server"),
        photo.get("id"),
        photo.get("secret"),
        size)

    return photoURL

# Generate URL for Flickr API search request
def get_flickr_search_request_url():
    requestURL = "https://www.flickr.com/services/rest/?method=flickr.photos.search&format=json&api_key="
    requestURL += FLICKR_API_KEY;                   # Add API key
    requestURL += "&safe_search=1"                  # Safe for work results
    requestURL += "&content_type=1"                 # Photos only
    requestURL += "&nojsoncallback=1"
    requestURL += "&per_page=" + str(resultsPerPage) # Results per page
    requestURL += "&tag_mode=any"                    # Any combination of tags
    requestURL += "&tags=shiba,shibainu,akita,akitainu"

    return requestURL


def make_photo_URL(farm, server, img_id, secret, size):
    url = "https://farm%s.staticflickr.com/%s/%s_%s_%s.jpg" % (farm, server, img_id, secret, size)

    return url

# def make_author_URL():

def main():
    print(get_image())

if __name__ == '__main__':
    main()