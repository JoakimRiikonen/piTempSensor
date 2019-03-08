import os
import sys
import tkinter as tk
from tkinter import ttk
import threading

def getSensor():
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            sensor = i
        return sensor

def readSensor(sensor):
    location = '/sys/bus/w1/devices/' + sensor + '/w1_slave'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature/1000
    return celsius

class GUI:
    def __init__(self):
        # init sensor
        self.sensor = getSensor()


        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)
        self.root.title("piTempSensor")
        self.root.geometry("480x320")
        self.mainframe = tk.Frame(self.root, bg='black')
        self.mainframe.pack_propagate(0)
        self.mainframe.pack(fill=tk.BOTH, expand=1)

        self.tempLabel = tk.Label(self.mainframe, text="23.4C",bg="black",
                                    fg="white", font=("Arial", 200))

        self.tempLabel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # esc to exit
        self.root.bind("<Escape>", self.exit)

        self.update_text()

        self.root.mainloop()

    def exit(self, event):
        self.root.destroy()
        exit()

    def update_text(self):
        self.tempLabel['text'] = "%0.1f C" % readSensor(self.sensor)
        t = threading.Timer(5, self.update_text)
        t.daemon=True
        t.start()



if __name__ == '__main__':
    gui = GUI()
