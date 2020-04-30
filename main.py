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
    print('\033[31m')
    print(f"{alert['properties']['event']}")
    print('\033[0m')
    print(f"\nHeadline:\n{alert['properties']['headline']}")
    print(f"\nDescription:\n{alert['properties']['description']}")
    print(f"\nArea:\n{alert['properties']['areaDesc']}")
    print(f'Last reload at {now}')

sleep_time = int(input("How long between checks(300 = 5 min): "))
state = input("What state are we watching(all caps abbr): ")

### Main Loop ###
while (True):
    now = time.asctime(time.localtime(time.time()))

    # Gets info and stores it into variables
    response = requests.get(get_url(state))    
    alert_data = response.json()

    alert_data_ids = alert_data['features']

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

    # How long till recheck
    time.sleep(sleep_time)

