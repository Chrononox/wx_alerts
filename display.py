#import tkinter as tk
from tkinter import *
import time


sleep_time = 240000 #in miliseconds please

def show_window(window):
    window.after(sleep_time, lambda: window.destroy()) # destroy the widget after 30 seconds
    window.mainloop()
    

# TODO Change the colors for the warnings n such
def alert_display_window(current_alerts):

    window = Tk()
    window.title("ALERT!!")    

    for alert in current_alerts:
        print(alert['properties']['event'])

        alert_frame = Frame(window, bd=2, relief=GROOVE)
        
        lbl_severity = Label(alert_frame, text=alert['properties']['event'], justify=LEFT)
        lbl_severity.pack()
        lbl_headline = Label(alert_frame, text=alert['properties']['headline'])
        lbl_headline.pack()

        alert_frame.pack(padx=1, pady=1)
    reload_btn = Button(text="Reload", command=window.destroy)
    reload_btn.pack()

    show_window(window)
    #destroy_window(window)
    #window.mainloop()


    
