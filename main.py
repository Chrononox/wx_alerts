#grab and display weather alerts

# TODO: Allow nationwide or per state (?multi-state?) -- This is now all automatic
#       Remember active seen alerts to avoid re-beeps
#       Need to prioritize T-warn over all and s-war/ t-watch over s-watch, 
#       Need to make sure special weather statemens are getting thouugh
#       need to make sure we are getting most local info i.e.'Freeze Warning', 'High Wind Warning', 'Excessive Heat Warning', 'Fire Weather Warning', Special Weather Statement'
#       Set Home and prioritize home alerts -- This is complete
#       Re-Evaluate info to be shown and display formatting -- working
#       Make better comments and notes
#       More useful info Number of warnings and watches in area
#       Colors ansi codes '\033[0m' set up color variables please

# Get active alerts nation wide = 'https://api.weather.gov/alerts/active?status=actual&message_type=alert&region_type=land'
# Get active alerts per state   = 'https://api.weather.gov/alerts/active/area/{state}'


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
    print(f"\nInstruction:\n{alert['properties']['instruction']}")
    print(f"\nArea:\n{alert['properties']['areaDesc']}")
    
# applies color and sound effects to different warn/watch types 
def effects(alert):
             
    if (alert['properties']['event'] == 'Tornado Warning'):
        play_sound(2400,1000)
        display_alert(alert, '\033[95m')

    elif (alert['properties']['event'] == 'Severe Thunderstorm Warning'):
        play_sound(1000, 500)
        display_alert(alert, '\033[31m')
    
    elif (alert['properties']['event'] == 'Tornado Watch'):
        play_sound(200, 500)
        display_alert(alert, '\033[96m')
        
    elif (alert['properties']['event'] == 'Severe Thunderstorm Watch'):
        display_alert(alert, '\033[33m')
    else:
        display_alert(alert)

def debug_mode():
    print("\n\n^.^ DEBUG MODE ^.^\n\n")
    val = input('^.^_')

    if val.lower() == 'test -t':
        print("Running fake - Tor Warn")
        effects(tor_test)
    elif val.lower() == 'test -s':
        print("Running fake - Storm Warn")
        effects(strm_test)
    elif (val.lower() == 'print'):
        print(tor_test)

    elif val.lower() == 'help':
        print('\ntest - run test')
        print('\nprint - print alert')

    ## ##
# Variables
counter = 0
sleep_time = 240
local_alert = False
state_alert = False
run = True
current_alerts = []
tor_test = {
    "properties":{
        "areaDesc": "Lee's Summit",
        "event": "Tornado Warning",
        "headline":"THIS IS A TEST",
        "instruction":"DO NOTHING",
        "response": "TEST",
        "severity": "TEST"
    }
}
strm_test = {
    "properties":{
        "areaDesc": "Lee's Summit",
        "event": "Severe Thunderstorm Warning",
        "headline":"THIS IS A TEST",
        "instruction":"DO NOTHING",
        "response": "TEST",
        "severity": "TEST"
    }
}


## adjustable vars ##
city = "Lee's Summit"
county = "Jackson, MO"
state = "MO"

## Start up ##
_ = system('cls') # clears the screen for new updated info
prompt = input("Weather alerts v2. enter to continue (debug):")

if(prompt.lower() == 'debug'):
    run = False
    debug_mode()

#!! Main Loop !!#
while(run):

    _ = system('cls') # clears the screen for new updated info
    curr_time = time.asctime(time.localtime(time.time())) # grab time of last refresh

    # Gets info and stores it into variables   
    response = requests.get(get_url_state(state)) 
    alert_data = response.json()
    alert_data_ids = alert_data['features']

    # City/County then State then US -working
    print("Looking for " + city + " & " + county)
    for alert in alert_data_ids:
        if(city in alert['properties']['description'] or county in alert['properties']['areaDesc']):
            local_alert = True
            current_alerts.append(alert['id'])
            effects(alert)            
        
    if(local_alert == False):
        print("Looking for " + state)
        for alert in alert_data_ids:
            if(state in alert['properties']['description']):
                state_alert = True
                current_alerts.append(alert['id'])
                effects(alert)

    if(local_alert == False and state_alert == False):
        print("EVERYWHERE...")
        response = requests.get(get_url_us())
        alert_data = response.json()
        alert_data_ids = alert_data['features']

        for alert in alert_data_ids:
            current_alerts.append(alert['id'])
            effects(alert)

    print(f'\nLast check at {curr_time}')

    # Reset alerts
    local_alert = False
    # Reccheck Timer
    time.sleep(sleep_time)