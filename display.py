import tkinter as tk
import requests
def test(num = 0):
    print(f"Connected! {num}")

def test_window():
    response = requests.get('https://api.weather.gov/alerts/active/area/MO')
    print("Running test window..")
    alert_data = response.json()
    alert_data_ids = alert_data['features']
    window=tk.Tk()
    window.title("Alert Window")

    for alert in alert_data_ids:
        label = tk.Label(text=alert['properties']['event'])
        lbl_severity = tk.Label(text=alert['properties']['severity'])
        lbl_headline = tk.Label(text=alert['properties']['headline'])
        lbl_severity.pack()
        label.pack()
        lbl_headline.pack()

    label2 = tk.Label(text="^.^")
    label2.pack()
    window.mainloop()