#grab and display weather alerts

import json
import requests
#import datetime
import time
from os import system, name
import winsound

# TODO:  ADD COUNTY FILTER FOR HOME SETTING, CLEAN UP CODE, ADD DEFAULT VALUES

def play_sound(frequency = 2500, duration = 1000):
    winsound.Beep(frequency, duration)

def get_url(state):
    temp = (f'https://api.weather.gov/alerts/active/area/{state}')
    return temp

def display_alert(alert, color):
    print('\n\n--------------------------------------------------')
    print(f"{alert['properties']['severity']}")
    print(f'{color}')
    print(f"{alert['properties']['event']}")
    print('\033[0m')
    print(f"\nHeadline:\n{alert['properties']['headline']}")
    print(f"\nDescription:\n{alert['properties']['description']}")
    print(f"\nArea:\n{alert['properties']['areaDesc']}")
    if ('Jackson, MO' in alert['properties']['areaDesc']):
        print('\033[91m')
        print("YOUR COUNTY!!")
        print('\033[0m')
    print(f'Last check at {now}')

sleep_time = int(input("How long between checks(300 = 5 min): "))
state = input("What state are we watching(all caps abbr): ").upper()
counter = 0;
### Main Loop ###
while (True):
    now = time.asctime(time.localtime(time.time()))
    counter += 1
    # Gets info and stores it into variables
    response = requests.get(get_url(state))    
    alert_data = response.json()

    alert_data_ids = alert_data['features']

    _ = system('cls') # clears the screen for new updated info
    print(f'Check #{counter} every {sleep_time} sec, at {now}, Showing Watches/Warns for {state}')

    for alert in alert_data_ids:
        if (alert['properties']['event'] == 'Severe Thunderstorm Warning'):
            play_sound(1000, 500)
            display_alert(alert, '\033[31m')
        
        if (alert['properties']['event'] == 'Severe Thunderstorm Watch'):
            display_alert(alert, '\033[33m')
            
        if (alert['properties']['event'] == 'Tornado Warning'):
            play_sound()
            display_alert(alert, '\033[95m')

        if (alert['properties']['event'] == 'Tornado Watch'):
            play_sound(200, 500)
            display_alert(alert)


    # How long till recheck
    
    time.sleep(sleep_time)

