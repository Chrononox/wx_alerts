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

def no_alerts_display_window():

    window = Tk()
    
    window.title("ALL CLEAR")  
    alert_frame = Frame(window, bd=2, relief=GROOVE)
    lbl_news = Label(alert_frame, text="^.^ All Clear Right Now. Checking Again Soon ^.^")
    lbl_news.pack()
    alert_frame.pack()

    reload_btn = Button(text="Reload", command=window.destroy)
    reload_btn.pack()


def alert_display_window(current_alerts):

    window = Tk()  

    for alert in current_alerts:

        print(f"{alert['properties']['event']}, {alert ['properties']['areaDesc']}\n\n")
        window.title("ALERT!!") 


        alert_frame = Frame(window, bd=2, relief=GROOVE)
        
        lbl_event = Label(alert_frame, text=alert['properties']['event'])
        lbl_event.pack()
        lbl_area = Label(alert_frame, text=alert['properties']['areaDesc'])
        lbl_area.pack()
        lbl_headline = Label(alert_frame, text=alert['properties']['headline'])
        lbl_headline.pack()


        alert_frame.pack(padx=1, pady=1)
    reload_btn = Button(text="Reload", command=window.destroy)
    reload_btn.pack()


    _ = system('cls') # clears the screen for new updated info
    print("WX-ALerts Running.  Monitering for severe weather localy and nation-wide!")
    print('^.^')

    # if(is_alerts == False):
    #     window.title("ALL CLEAR")  
    #     alert_frame = Frame(window, bd=2, relief=GROOVE)
    #     lbl_news = Label(alert_frame, text="^.^ All Clear Right Now. Checking Again Soon ^.^")
    #     lbl_news.pack()
    #     alert_frame.pack()

    show_window(window)
