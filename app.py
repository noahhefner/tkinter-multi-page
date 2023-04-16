import tkinter as tk
from selector import Selector

class App (tk.Tk):

    def __init__ (self, config):
        """
        Setup Tkinter frames. The selector Frame holds a dropdown menu to
        select which page Frame below should be shown. For each Frame in pages,
        a Frame is created.
        """

        super().__init__()
      
        # Setup grid
        for r in range(8):
            self.rowconfigure(r, weight = 1)
        for c in range(1):
            self.columnconfigure(c, weight = 1)

        # Create selector frame
        self.frame_selector = Selector(
            [key for key, value in config.items()],
            self.on_page_select_change,
        )
        self.frame_selector.grid(row = 0, column = 0)

        # Create page frames
        self.frame_pages = {}
        for key, value in config.items():
            page = value(key)
            self.frame_pages[key] = page
            self.frame_pages[key].grid(row = 1, column = 0, sticky = "nsew")

    def on_page_select_change (self, event):
        """
        Raise the appropriate page frame given the ID.
        """

        selected_id = self.frame_selector.selected_page.get()
        self.frame_pages[selected_id].tkraise()
