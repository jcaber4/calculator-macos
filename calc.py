from tkinter import *
from buttons import *


class Calc(Frame):
    """Holds the buttons and screen"""

    def __init__(
        self,
        screen,
        master=None,
    ):
        super().__init__(master)
        self.master = master
        self.buttons = []
        screen.grid(columnspan=6, ipadx=68, ipady=10, row=0)
        self.display = screen
        self.load_buttons()
        for row_pos in range(1, 4):
            for column_pos in range(3):
                self.buttons.pop(1).grid(row=row_pos, column=column_pos)
        self.buttons.pop(0).grid(row=4, column=0)
        self.buttons.pop(0).grid(row=4, column=1)
        self.buttons.pop().grid(row=4, column=2)
        for row_pos in range(1, 5):
            self.buttons.pop(0).grid(row=row_pos, column=4)
        for row_pos in range(1, len(self.buttons) + 1):
            self.buttons.pop(0).grid(row=row_pos, column=5)

    def load_buttons(self):
        for i in range(10):
            self.buttons.append(NumberButton(self.master, self.display, i))
        self.buttons.append(NumberButton(self.master, self.display, "."))
        for operation in "+-*/":
            self.buttons.append(OperationButton(self.master, self.display, operation))
        self.buttons.append(BackspaceButton(self.master, self.display))
        self.buttons.append(ClearButton(self.master, self.display))
        self.buttons.append(EnterButton(self.master, self.display))
