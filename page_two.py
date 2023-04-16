import tkinter as tk
import Page

class PageTwo (Page):

    def __init__ (self, id, parent):

        super().__init__(self, id, parent)

    def get_id (self):

        return self.id
