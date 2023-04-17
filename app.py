import tkinter as tk
from selector import Selector

class App (tk.Tk):

    def __init__ (self, pages):
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

        # Create page frames
        self.frame_pages = {}
        for page in pages:
            p = page()
            id = p.get_id()
            self.frame_pages[id] = p
            self.frame_pages[id].grid(row = 1, column = 0, sticky = "nsew")

        # Create selector frame
        self.frame_selector = Selector(
            [key for key, value in self.frame_pages.items()],
            self.on_page_select_change,
        )
        self.frame_selector.grid(row = 0, column = 0)

    def on_page_select_change (self, event):
        """
        Raise the appropriate page frame given the ID.
        """

        selected_id = self.frame_selector.selected_page.get()
        self.frame_pages[selected_id].tkraise()
