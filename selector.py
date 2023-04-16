# Drop down for selecting which page to go to

import tkinter as tk
from tkinter import ttk

class Selector (tk.Frame):

    def __init__ (self, dropdown_values, callback):

        super().__init__()
 
        self.selected_page = tk.StringVar()
        self.page_selector = ttk.Combobox(self, textvariable = self.selected_page)
        self.page_selector['values'] = dropdown_values
        self.page_selector.bind('<<ComboboxSelected>>', callback)
        self.page_selector.pack()
      
