from tkinter import *


class Screen(Entry):
    """Holds Screen Contents"""

    def __init__(self, master=None, cnf={}, **kw):
        Widget.__init__(self, master, "entry", cnf, kw)
        self.visable = ""
        self.textvariable = kw["textvariable"]

    def push(self, to_push):
        self.visable = self.get() + str(to_push)
        self.textvariable.set(self.visable)

    def delete(self):
        newstr = self.get()
        self.visable = newstr[:-1]
        self.textvariable.set(newstr[:-1])

    def clear(self):
        self.visable = ""
        self.textvariable.set("")

    def evaluate(self):
        try:
            result = str(eval(self.get()))
            self.textvariable.set(result)
            self.visable = ""
        except:
            self.textvariable.set(" error ")
            self.visable = ""
