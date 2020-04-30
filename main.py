#grab and display weather alerts

import json
import requests
#import datetime
import time
from os import system, name

# TODO: ADD COLORS FOR ALERTS, ADD COUNTY FILTER FOR HOME SETTING, CLEAN UP CODE,
#        ADD AUTO CAP FOR STATS, ADD DEFAULT VALUES, FILTER ALERT TYPES
# NOTE: For each seperate alert is a new id, need to cycle through them

def get_url(state):
    temp = (f'https://api.weather.gov/alerts/active/area/{state}')
    return temp

# url ='https://api.weather.gov/alerts/MO'
# url_KS = 'https://api.weather.gov/alerts/active/area/KS'
# url_MO = 'https://api.weather.gov/alerts/active/area/MO'
# url_CO = 'https://api.weather.gov/alerts/active/area/CO'

sleep_time = 300 # in seconds
sleep_time = int(input("How long between checks(300 = 5 min): "))
state = input("What state are we watching(all caps abbr): ")

while (True):
    now = time.asctime(time.localtime(time.time()))
    # Gets info and stores it into variables
    response = requests.get(get_url(state))    
    alert_data = response.json()

    alert_data_ids = alert_data['features']
    alert_data_counties = alert_data["features"][0]['properties']['areaDesc']
    event = alert_data['features'][0]['properties']['event']
    headline = alert_data['features'][0]['properties']['headline']
    description = alert_data['features'][0]['properties']['description']
    instruction = alert_data['features'][0]['properties']['instruction']
    secerity = alert_data['features'][0]['properties']['severity']

    _ = system('cls') # clears the screen for new updated info
    print(f'Last reload at {now}')
    for alert in alert_data_ids:
        print('\n\n--------------------------------------------------')
        print(f"\nHeadline:\n{alert['properties']['headline']}")
        print(f"\nDescription:\n{alert['properties']['description']}")
        print(f"\nArea:\n{alert['properties']['areaDesc']}")
        if('Jackson, MO' in alert['properties']['areaDesc']): # this will be used to find home county alerts
            print("\n\nCOUNTY FOUND!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n")
        print(f'Last reload at {now}')
        print('\n\n--------------------------------------------------')



    # Displays info on screen
    # _ = system('cls') # clears the screen for new updated info
    # _ = system('COLOR 1') # turn text blue?
    # print(f'Last reload at {now}')
    # print(f'\n{headline}')
    # print(f'\n{description}')
    # print(f'\n{instruction}')
    # print('\n\nControl + C to quit')

    # How long till recheck
    time.sleep(sleep_time)

