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

# Imports #
import json
import requests
import time
from os import system, name
import winsound

## FUNCTIONS ##

# Grab alerts based on state
def get_url_state(state = 'MO'):
    temp = (f'https://api.weather.gov/alerts/active/area/{state}')
    return temp
# Grab alerts based on US
def get_url_us():
    temp = (f'https://api.weather.gov/alerts/active?status=actual&message_type=alert&region_type=land')
    return temp


# Variables #
sleep_time = 240 #time till alert refresh
local_alert = False
state_alert = False

## Adjustable Variables ##
city = "Plato"
county = "Jackson, Mo"
state = "MO"


#!! MAIN LOOP !!#
while(True):

     _ = system('cls') # clears the screen for new updated info
    curr_time = time.asctime(time.localtime(time.time())) # grab time of last refresh

    # Gets info and stores it into variables   
    response = requests.get(get_url_state(state)) 
    alert_data = response.json()
    alert_data_ids = alert_data['features']

    # City/County then State then US -working
    if(not local_alert):
        for alert in alert_data_ids:
            if(city in alert['properties']['description'] or county in alert['properties']['areaDesc']):                
                local_alert = True
                display_alert(alert)

    if(not local_alert):
        for alert in alert_data_ids:
            if(state in alert['properties']['description']):
                state_alert = True
                display_alert(alert)

    if(not local_alert and not state_alert):
        response = requests.get(get_url_us())
        alert_data = response.json()
        alert_data_ids = alert_data['features']

        for alert in alert_data_ids:
            display_alert(alert)

    
    print(f'\nLast check at {curr_time}')

    # recheck timer
    time.sleep(slee_time)