import tkinter as tk
from tkinter import font as tkFont

'''
This file provides a overrided Text Class from tkinter named
RichText and is used in the About tab.
'''

class RichText(tk.Text):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        default_font = tkFont.nametofont(self.cget("font"))

        em = default_font.measure("m")
        default_size = default_font.cget("size")
        bold_font = tkFont.Font(**default_font.configure())
        italic_font = tkFont.Font(**default_font.configure())
        h1_font = tkFont.Font(**default_font.configure())
        h2_font = tkFont.Font(**default_font.configure())
        h3_font = tkFont.Font(**default_font.configure())

        bold_font.configure(weight="bold")
        italic_font.configure(slant="italic")
        h1_font.configure(size=int(default_size*2), weight="bold")
        h2_font.configure(size=int(default_size*1.5), weight="bold")
        h3_font.configure(size=int(default_size*1.2), weight="bold")

        self.tag_configure("bold", font=bold_font)
        self.tag_configure("italic", font=italic_font)
        self.tag_configure("h1", font=h1_font, spacing3=default_size)
        self.tag_configure("h2", font=h2_font, spacing3=default_size)
        self.tag_configure("h3", font=h3_font, spacing3=default_size)

        lmargin2 = em + default_font.measure("\u2022 ")
        self.tag_configure("bullet", lmargin1=em, lmargin2=lmargin2)

    def insert_bullet(self, index, text):
        self.insert(index, f"\u2022 {text}", "bullet")
