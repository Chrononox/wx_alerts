



def get_alerts_us():
    '''Returns the alerts for the whole US'''
    temp = (f'https://api.weather.gov/alerts/active?status=actual&message_type=alert&region_type=land')
    return temp
