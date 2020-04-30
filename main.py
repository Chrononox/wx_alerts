#grab and display weather alerts

import json
import requests
#import datetime
import time
from os import system, name

# TODO: ADD COLORS FOR ALERTS, ADD COUNTY FILTER FOR HOME SETTING, CLEAN UP CODE,
#        ADD AUTO CAP FOR STATS, ADD DEFAULT VALUES, FILTER ALERT TYPES
#
# NOTE: For each seperate alert is a new id, need to cycle through them
#       Maybe show all alerts unless watched area is found then only show watched area?

def get_url(state):
    temp = (f'https://api.weather.gov/alerts/active/area/{state}')
    return temp

def display_alert(alert):
    print('\n\n--------------------------------------------------')
    print(f"{alert['properties']['severity']}")
    print(f"{alert['properties']['event']}")
    print(f"\nHeadline:\n{alert['properties']['headline']}")
    print(f"\nDescription:\n{alert['properties']['description']}")
    print(f"\nArea:\n{alert['properties']['areaDesc']}")
    print(f'Last reload at {now}')
    #print('\n\n--------------------------------------------------')

sleep_time = int(input("How long between checks(300 = 5 min): "))
state = input("What state are we watching(all caps abbr): ")

### Main Loop ###
while (True):
    now = time.asctime(time.localtime(time.time()))

    # Gets info and stores it into variables
    response = requests.get(get_url(state))    
    alert_data = response.json()

    alert_data_ids = alert_data['features']
    # alert_data_counties = alert_data["features"][0]['properties']['areaDesc']
    # event = alert_data['features'][0]['properties']['event']
    # headline = alert_data['features'][0]['properties']['headline']
    # description = alert_data['features'][0]['properties']['description']
    # instruction = alert_data['features'][0]['properties']['instruction']
    # secerity = alert_data['features'][0]['properties']['severity']

    _ = system('cls') # clears the screen for new updated info
    print(f'Last reload at {now}, Showing Warnings/Watches for {state}')

    for alert in alert_data_ids:
        if (alert['properties']['event'] == 'Severe Thunderstorm Warning'):
            display_alert(alert)
        
        if (alert['properties']['event'] == 'Severe Thunderstorm Watch'):
            display_alert(alert)
            
        if (alert['properties']['event'] == 'Tornado Warning'):
            display_alert(alert)

        if (alert['properties']['event'] == 'Tornado Watch'):
            display_alert(alert)

        if (alert['properties']['severity'] == 'Extreme'):
            display_alert(alert)

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

