#import tkinter as tk
from tkinter import *
import time
from os import system, name


sleep_time = 240000 #in miliseconds please
is_alerts = False

def show_window(window):
    window.after(sleep_time, lambda: window.destroy()) # destroy the widget after 30 seconds
    window.mainloop()
    

# TODO Change the colors for the warnings n such

def alert_display_window(current_alerts):

    window = Tk()
    #scrollbar = Scrollbar(window)
    #scrollbar.pack(side = RIGHT, fill=Y)
    # window.title("ALERT!!")    

    for alert in current_alerts:

        #print(alert['properties']['event'])

        print(f"{alert['properties']['event']}, {alert ['properties']['areaDesc']}\n\n")
        window.title("ALERT!!")  


        alert_frame = Frame(window, bd=2, relief=GROOVE)
        
        # lbl_severity = Label(alert_frame, text=alert['properties']['severity'], justify=LEFT)
        # lbl_severity.pack()
        lbl_event = Label(alert_frame, text=alert['properties']['event'])
        lbl_event.pack()
        lbl_area = Label(alert_frame, text=alert['properties']['areaDesc'])
        lbl_area.pack()
        lbl_headline = Label(alert_frame, text=alert['properties']['headline'])
        lbl_headline.pack()
        # lbl_instructions = Label(alert_frame, text=alert['properties']['instruction'])
        # lbl_instructions.pack()
        

        alert_frame.pack(padx=1, pady=1)
    reload_btn = Button(text="Reload", command=window.destroy)
    reload_btn.pack()


    _ = system('cls') # clears the screen for new updated info
    print("Starting WX-Alerts.  Monitering for severe weather localy and nation-wide!")
    print('^.^')

    if(is_alerts == False):
        window.title("ALL CLEAR")  
        alert_frame = Frame(window, bd=2, relief=GROOVE)
        lbl_news = Label(alert_frame, text="^.^ All Clear Right Now. Checking Again Soon ^.^")
        lbl_news.pack()
        alert_frame.pack()

    show_window(window)
    #destroy_window(window)
    #window.mainloop()