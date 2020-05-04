#grab and display weather alerts

# TODO: Allow nationwide or per state (?multi-state?)
#       Remember active seen alerts to avoid re-beeps
#       Set Home and prioritize home alerts
#       Re-Evaluate info to be shown and display formatting
#       Make better comments and notes
#       More useful info Number of warnings and watches in area

# Get active alerts nation wide = 'https://api.weather.gov/alerts/active?status=actual&message_type=alert&region_type=land'
# Get active alerts per state   = 'https://api.weather.gov/alerts/active/area/{state}'

# TODO:  ADD COUNTY FILTER FOR HOME SETTING, CLEAN UP CODE, ADD DEFAULT VALUES

# Imports
import json
import requests
import time
from os import system, name
import winsound

## FUNCTIONS ##

# Plays sounds
def play_sound(frequency = 2500, duration = 1000):
    winsound.Beep(frequency, duration)

# Grabs form the alerts for the state alone
def get_url_state(state):
    temp = (f'https://api.weather.gov/alerts/active/area/{state}')
    return temp

# Grabs from the alerts for the whole US
def get_url_us():
    temp = (f'https://api.weather.gov/alerts/active?status=actual&message_type=alert&region_type=land')
    return temp

# Controls what the display looks like
def display_alert(alert, color = '\033[0m'):
    print('\n\n--------------------------------------------------')
    #print(message)
    print(f"{alert['properties']['severity']} -- {alert['properties']['response']}")
    print(f'{color}')
    print(f"{alert['properties']['event']}")
    print('\033[0m')    
    print(f"\nHeadline:\n{alert['properties']['headline']}")
    print(f"\nArea:\n{alert['properties']['instruction']}")
    print(f"\nArea:\n{alert['properties']['areaDesc']}")
    
    # applies color and sound effects to different warn/watch types 
def effects(alert):
             
    if (alert['properties']['event'] == 'Tornado Warning'):
        play_sound(2400,1000)
        display_alert(alert, '\033[95m')

    if (alert['properties']['event'] == 'Severe Thunderstorm Warning'):
        play_sound(1000, 500)
        display_alert(alert, '\033[31m')
    
    if (alert['properties']['event'] == 'Tornado Watch' and warn_found == False):
        play_sound(200, 500)
        display_alert(alert, '\033[96m')
        
    if (alert['properties']['event'] == 'Severe Thunderstorm Watch' and warn_found == False and tor_found == False):
        display_alert(alert, '\033[33m')

    ## ##
# Variables
counter = 0
sleep_time = 240
local_alert = False
state_alert = False

## adjustable vars ##
city = "Lee's Summit"
county = "Jackson, MO"
state = "MO"

## Start up ##


#!! Main Loop !!#
while(True):

    _ = system('cls') # clears the screen for new updated info
    curr_time = time.asctime(time.localtime(time.time())) # grab time of last refresh

    # Gets info and stores it into variables   
    response = requests.get(get_url_state(state)) 
    alert_data = response.json()
    alert_data_ids = alert_data['features']

    # City/County then State then US -working
    #print("Looking for " + city + " & " + county)
    for alert in alert_data_ids:
        if(city in alert['properties']['description'] or county in alert['properties']['areaDesc']):
            local_alert = True
            #display_alert(alert)
            effects(alert)
            
        
    if(local_alert == False):
        #print("Looking for " + state)
        for alert in alert_data_ids:
            if(state in alert['properties']['description']):
                state_alert = True
                #display_alert(alert)
                effects(alert)

    if(local_alert == False and state_alert == False):
        response = requests.get(get_url_us())
        alert_data = response.json()
        alert_data_ids = alert_data['features']

        for alert in alert_data_ids:
            #display_alert(alert)
            effects(alert)

    print(f'\nLast check at {curr_time}')

     # Reset alerts
    local_alert = False
    # Reccheck Timer
    time.sleep(sleep_time)