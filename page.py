import tkinter as tk

class Page (tk.Frame):

    def __init__ (self, id):

        super().__init__()

        self.id = id

    def get_id (self):

        return self.id


