import os
import tkinter as tk
from tkinter import ttk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)
        self.root.title("piTempSensor")
        self.root.geometry("480x320")
        self.mainframe = tk.Frame(self.root, bg='black')
        self.mainframe.pack_propagate(0)
        self.mainframe.pack(fill=tk.BOTH, expand=1)

        self.tempLabel = tk.Label(self.mainframe, text="23.4C",bg="black",
                                    fg="white", font=("Arial", 100))

        self.tempLabel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.root.mainloop()

if __name__ == '__main__':
    gui = GUI()
