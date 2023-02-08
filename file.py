from ast import Delete
from distutils.cmd import Command
from http.client import ImproperConnectionState
import tkinter as tk
from tkinter.ttk import Widget
from turtle import back, onclick

import json

import os
os.chdir("./Programming/Python/")
del os
running = True
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simplenote")
        self.geometry("600x800")

        self.text = tk.Text(self, height="800", width="600", bg="#555")
        self.text.pack()
        self.text.config(foreground="#fff")
        self.text.focus()


################################################################################################
# The default start for the app
# Will display all the previous notes and an empty note in order to create a new note
################################################################################################
class NoteApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simplenote")
        self.geometry("600x800")
        self.config(bg="#777")

        # load in text fields from storage.json
        self.btn = tk.Button(self, text="Empty note...", anchor="w", width="600", height="3", background="#777", activebackground="#777", highlightbackground="#777")
        self.btn.bind("<Button-1>", lambda e:callback(e))
        self.btn.pack()

        data = json.load(open("storage.json"))
    

        self.buttons = []
        for i in range(0, len(data["data"])):
            temp = tk.Button(self, text=data["data"][i], anchor="w", width="600", height="3", background="#777", activebackground="#777", highlightbackground="#777",
            command= lambda txt=data["data"][i]: self.openNote(txt))
            temp.pack()
            self.buttons.append(temp)


    def openNote(self, txt):
        print("Opening note...", txt)
        stopApp(txt)


def callback(event):
    print(event)

def openNote(event):
    pass

app = NoteApp()

def stopApp(txt):
    global app
    app.destroy()

    note = App()
    note.mainloop()

def main():
    global app
    app.mainloop()

if __name__ == "__main__":
    main()