import tkinter as tk
import PageOne

class App (tk.Tk):

    def __init__ (self, *pages):

        tk.Tk.__init__(self)

        self.container = tk.Frame(self)
        self.container.pack(side = "top", fill = "both", expand = True)
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)

        # Drop down for selecting which page to go to
        self.selected_page = tk.StringVar()
        self.page_selector = tk.ComboBox(self, textvariable = self.selected_page)
        self.page_selector.bind('<<ComboboxSelected>>', self.on_page_select_change)

        # Pages
        self.frames = {}

        for page in pages:

            frame = page(self.container, self)
            self.frames[page.get_id()] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.selected_page['values'] = [frame.get_id() for frame in self.frames]

    def switch_frame (self, frame):

        self.show_frame(frame)

    def on_page_select_change (self, event):

        selection = self.selected_page.get()
        print(selection)
