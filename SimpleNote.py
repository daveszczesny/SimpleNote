#  imports
from email.policy import default
import json
import tkinter as tk

grey = "#222"



class SimpleNoteMenu(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("SimpleNote")
        self.geometry("600x800")
        self.config(bg=grey)


        # new note button
        self.newNote = tk.Button(self, text="Empty note... ", anchor="nw",
            width="600", height="3", foreground="#aaa", activeforeground="#fff",background=grey, activebackground=grey,
            highlightbackground=grey, command=lambda:stop(self)).pack()

        # previous notes saved
       

        try:
            f = open("storage.json", "r")
            data = json.load(f)
            for i in range(0, len(data["data"])):
                temp = tk.Button(self, text=data["data"][i], anchor="nw", width="600", height="3", background=grey,
                    activebackground=grey, highlightbackground=grey, foreground="#aaa", activeforeground="#fff",
                    command= lambda txt=data["data"][i]: stop(self,t=txt, menu=False))
                temp.pack()
                f.close()
        except:
            pass

        


class Note(tk.Tk):
    def __init__(self, txt) -> None:
        super().__init__()
        self.title("SimpleNote")
        self.geometry("600x800")
        self.config(bg=grey)

        self.defaultText = "" if len(txt)<0 else txt

        self.note = tk.Text(self, height="800", width="600", bg=grey, insertbackground="#fff")
        self.note.insert(tk.INSERT, txt)
        self.note.pack()
        self.note.config(foreground="#fff")
        self.note.focus()

        self.bind("<Escape>", lambda e: [save(self.note.get("1.0",tk.END), defaultText=self.defaultText),stop(self, menu=True)])

def save(txt, defaultText):
    overwrite = False if  defaultText == "" else True
    try:
        f = open("storage.json", "r")
        data=json.load(f)
        f.close()

        if (len(defaultText) > 0 and len(txt) <= 1):
            f=open("storage.json", "w")

            data["data"].remove(defaultText)

            json.dump(data,f)

            f.close()

        elif overwrite:
            f=open("storage.json", "w")
            # find index of defaulText

            data["data"][data["data"].index(defaultText)] = txt
            json.dump(data,f)

            f.close()
        else:
            if (len(txt) > 1): 
                f = open("storage.json", "w")
                data["data"].append(txt)
                print(data)
                json.dump(data, f)
                f.close()

    except:
        if(len(txt)>1):
            # shud only run if there are no previous notes saved
            f = open("storage.json", "w")
            data = {"data":[txt]}
            json.dump(data, f)
            f.close()


    

        

def stop(app, t="", menu=False):
    app.destroy()
    if menu:
        main(menu=True)
    else:
        main(menu=False, txt=t)

def main(menu=True, txt=""):
    if menu:
        app = SimpleNoteMenu()
    else:
        app = Note(txt)

    app.mainloop()


if __name__ == "__main__":
    main()
