#grab and display weather alerts

# Get active alerts nation wide = 'https://api.weather.gov/alerts/active?status=actual&message_type=alert&region_type=land'
# Get active alerts per state   = 'https://api.weather.gov/alerts/active/area/{state}'

# TODO: Error checking whit response.ok

# Imports
import json
import requests
import time
from os import system, name
import winsound

import display

# Variables
counter = 0
local_alert = False
state_alert = False
all_alert = False
run = True     # TURNS THE MAIN LOOP ON AND OFF
current_alerts = []


tw = 'Tornado Warning'
twa = 'Tornado Watch'
sw = 'Severe Thunderstorm Warning'
swa = 'Severe Thunderstorm Watch'
fw = 'Freeze Warning'
ww = 'High Wind Warning'
eh = 'Excessive Heat Warning'
fire = 'Fire Weather Warning'
sws = 'Special Weather Statement'

twarn_color = '\033[95m'
twatch_color = '\033[96m'
swarn_color = '\033[31m'
swatch_color = '\033[33m'

# Vars used for testing only
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

#### FUNCTIONS ####

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
        #display_alert(alert, twarn_color)
        current_alerts.append(alert)

    elif (alert['properties']['event'] == 'Severe Thunderstorm Warning'):
        play_sound(1000, 500)
        #display_alert(alert, swarn_color)
        current_alerts.append(alert)
    
    elif (alert['properties']['event'] == 'Tornado Watch'):
        play_sound(200, 500)
        #display_alert(alert, twatch_color)
        current_alerts.append(alert)
        
    elif (alert['properties']['event'] == 'Severe Thunderstorm Watch'):
        #display_alert(alert, swatch_color)
        current_alerts.append(alert)
    else:
        display_alert(alert)
        current_alerts.append(alert)

##@@ Start up @@##
_ = system('cls') # clears the screen for new updated info
#prompt = input("Weather alerts v2. enter to continue:")

# if(prompt.lower() == 'test -t'):
#     print("Running fake - Tor Warn")
#     effects(tor_test)
#     input("\nenter to continue")
# elif prompt.lower() == 'test -s':
#     print("Running fake - Storm Warn")
#     effects(strm_test)
#     input("\nenter to continue")

#display.test_window()

##!! Main Loop !!##

while(run):

    _ = system('cls') # clears the screen for new updated info
    curr_time = time.asctime(time.localtime(time.time())) # grab time of last refresh
    
    print("Checking for local alerts...")
    response = requests.get(get_url_state(state))

    if (response.ok):
        _ = system('cls') # clears the screen for new updated info
        alert_data = response.json()
        alert_data_ids = alert_data['features']
        
        
        # City/County then State then US
        for alert in alert_data_ids:
            if(city in alert['properties']['description'] or county in alert['properties']['areaDesc']):                 
                
                thing  = alert['properties']['event']
                if (thing == tw or thing == twa or thing == sw or thing == swa or thing == fw or thing == ww or thing == eh or thing == fire or thing == sws):    
                    #current_alerts.append(alert['id'])
                    effects(alert)
                    all_alert = True

        if(local_alert == False):
            for alert in alert_data_ids:
                if(state in alert['properties']['description'] or state in alert['properties']['areaDesc']):
                    
                    thing  = alert['properties']['event']
                    if (thing == tw or thing == twa or thing == sw or thing == swa or thing == fw or thing == ww or thing == eh or thing == fire or thing == sws):
                        state_alert = True
                        #current_alerts.append(alert['id'])
                        effects(alert)
                        all_alert = True
        
        if(local_alert == False and state_alert == False):
            _ = system('cls') # clears the screen for new updated info
            print("LOCAL FILTERS CLEAR. CHECKING EVERYWHERE...")
            response = requests.get(get_url_us())
            if(response):
                alert_data = response.json()
                alert_data_ids = alert_data['features']

                for alert in alert_data_ids:
                    thing  = alert['properties']['event']
                    #if (thing == tw or thing == twa or thing == sw or thing == swa or thing == fw or thing == ww or thing == eh or thing == fire or thing == sws):
                    if (thing == tw or thing == twa or thing == sw):
                        #current_alerts.append(alert['id'])
                        all_alert = True
                        effects(alert)
            else:
                _ = system('cls') # clears the screen for new updated info
                print("No Response, Will try again soon")
                all_alert == True
                print("Bad Response", response)

    else:
        _ = system('cls') # clears the screen for new updated info
        print("No Response, Will try again soon")
        all_alert == True
        print("Bad Response", response)

    if(all_alert == False):
        #print(response)
        _ = system('cls') # clears the screen for new updated info
        print("\n\n\u001b[38;5;200m^.^\033[0m All Clear Right Now. Checking Again Soon \u001b[38;5;200m^.^\033[0m")        

    display.alert_display_window(current_alerts)
    current_alerts = []
    print(f'\nLast check at {curr_time}')

    # Reset alerts
    local_alert = False
    state_alert = False
    all_alert = False

    # Reccheck Timer
#    time.sleep(sleep_time)
