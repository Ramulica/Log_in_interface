import tkinter as tk
import sqlite3
import os
from tkinter import ttk as ttk
from PIL import Image, ImageTk



class Interface:
    def __init__(self, background):

        self.background = background




        self.root = tk.Tk()
        self.root.geometry("600x700")

        self.main_frame = tk.Frame(self.root)
        self.main_frame.configure(bg=self.background[0])
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        # IMAGES
        self.main_path = os.getcwd()
        os.chdir("photos")
        self.logo_image = tk.PhotoImage(file="Logo_image.png")
        self.check_image = ImageTk.PhotoImage(Image.open("log_in_check.png"))
        os.chdir(self.main_path)

        self.main_interface()

        self.root.mainloop()

    def make_a_new_frame(self):
        self.main_frame.destroy()
        self.main_frame = tk.Frame(self.root)
        self.main_frame.configure(bg=self.background[0])
        self.main_frame.pack(expand=True, fill=tk.BOTH)





    def main_interface(self):

        self.make_a_new_frame()

        self.back_button = tk.Button(self.main_frame, text=" ◀ ", font=("Arial", 15), bg="red",
                                fg=self.background[2],
                                command=exit)
        self.back_button.grid(row=0, column=0)

        self.logo = tk.Label(self.main_frame, image=self.logo_image, borderwidth=0)
        self.logo.grid(column=2, row=1, padx=20, pady=20, columnspan=3, sticky=tk.EW)

        log_in_button = tk.Button(self.main_frame, text="Log In", font=("Arial", 20, "bold"), bg=self.background[1],
                                  fg=self.background[2], width=20,
                                  command=lambda: self.log_in_interface())
        log_in_button.grid(column=2, row=2, padx=20, pady=20, columnspan=3, sticky=tk.EW)
        sing_in_button = tk.Button(self.main_frame, text="Sing In", font=("Arial", 20, "bold"), bg=self.background[1],
                                   fg=self.background[2], width=20,
                                   command=lambda: self.sing_in_interface())
        sing_in_button.grid(column=2, row=3, padx=20, pady=20, columnspan=3, sticky=tk.EW)
        settings_button = tk.Button(self.main_frame, text="settings", font=("Arial", 20, "bold"), bg=self.background[1],
                                    fg=self.background[2], width=20,
                                    command=lambda: self.make_a_new_frame())
        settings_button.grid(column=2, row=4, padx=10, pady=20, columnspan=3, sticky=tk.EW)

    def log_in_interface(self):
        self.make_a_new_frame()

        self.back_button = tk.Button(self.main_frame, text=" ◀ ", font=("Arial", 15), bg="red",
                                fg=self.background[2],
                                command=lambda: self.main_interface())
        self.back_button.grid(row=0, column=0)

        self.logo = tk.Label(self.main_frame, image=self.logo_image, borderwidth=0)
        self.logo.grid(column=2, row=1, padx=20, pady=20, columnspan=3, sticky=tk.EW)

        self.username_frame = tk.Frame(self.main_frame, bg=self.background[1])
        self.username_frame.grid(column=2, row=2, padx=20, pady=20, columnspan=3, sticky=tk.EW)

        self.username_entry = PlaceholderEntry(self.username_frame, placeholder="Username", font=("Arial", 20, "bold"))
        self.username_entry.pack(fill=tk.BOTH, padx=5, pady=5)

        self.password_frame = tk.Frame(self.main_frame, bg=self.background[1])
        self.password_frame.grid(column=2, row=3, padx=20, pady=20, columnspan=3, sticky=tk.EW)

        self.password_entry = PlaceholderEntry(self.password_frame, placeholder="Password", font=("Arial", 20, "bold"),
                                               password=False)
        self.password_entry.pack(fill=tk.BOTH, padx=5, pady=5)

        self.log_in_button = tk.Button(self.main_frame, text="Log In", font=("Arial", 20, "bold"), bg=self.background[1],
                                  fg=self.background[2], width=20,
                                  command=lambda: self.verify_user())
        self.log_in_button.grid(column=2, row=4, padx=20, pady=20, columnspan=3, sticky=tk.EW)

    def verify_user(self):
        self.username_frame.configure(bg="red")
        # self.log_in_successful_interface()

    def log_in_successful_interface(self):
        self.make_a_new_frame()

    def sing_in_interface(self):
        self.make_a_new_frame()

        self.back_button = tk.Button(self.main_frame, text=" ◀ ", font=("Arial", 15), bg="red",
                                fg=self.background[2],
                                command=lambda: self.main_interface())
        self.back_button.grid(row=0, column=0)

        self.space_label = tk.Label(self.main_frame, bg=self.background[0], text=f"{'X'* 75}", fg=self.background[0])
        self.space_label.grid(row=0, column=2)

        self.email_frame = tk.Frame(self.main_frame, bg=self.background[1])
        self.email_frame.grid(column=2, row=1, padx=20, pady=20, columnspan=3, sticky=tk.EW)

        self.email_entry = PlaceholderEntry(self.email_frame, placeholder="Email", font=("Arial", 20, "bold"))
        self.email_entry.pack(fill=tk.BOTH, padx=5, pady=5)

        self.username_frame = tk.Frame(self.main_frame, bg=self.background[1])
        self.username_frame.grid(column=2, row=2, padx=20, pady=20, columnspan=3, sticky=tk.EW)

        self.username_entry = PlaceholderEntry(self.username_frame, placeholder="Username", font=("Arial", 20, "bold"))
        self.username_entry.pack(fill=tk.BOTH, padx=5, pady=5)

        self.password_frame = tk.Frame(self.main_frame, bg=self.background[1])
        self.password_frame.grid(column=2, row=3, padx=20, pady=20, columnspan=3, sticky=tk.EW)

        self.password_entry = PlaceholderEntry(self.password_frame, placeholder="Password", font=("Arial", 20, "bold"),
                                               password=False, show="*")
        self.password_entry.pack(fill=tk.BOTH, padx=5, pady=5)


        self.c1 = tk.Checkbutton(self.main_frame, text='Show Password', bg=self.background[0],
                                 command=self.password_entry.toggle)
        self.c1.grid(row=4, column=2, sticky=tk.W, padx=20)

        self.confirm_password_frame = tk.Frame(self.main_frame, bg=self.background[1])
        self.confirm_password_frame.grid(column=2, row=5, padx=20, pady=20, columnspan=3, sticky=tk.EW)

        self.confirm_password_entry = PlaceholderEntry(self.confirm_password_frame, placeholder="Confirm password", font=("Arial", 20, "bold"), password=False, show="*")
        self.confirm_password_entry.pack(fill=tk.BOTH, padx=5, pady=5)

        self.c2 = tk.Checkbutton(self.main_frame, text='Show Password Confirmation', bg=self.background[0],
                                command=self.confirm_password_entry.toggle)
        self.c2.grid(row=6, column=2, sticky=tk.W, padx=20)

        self.sing_in_button = tk.Button(self.main_frame, text="Sing In", font=("Arial", 20, "bold"), bg=self.background[1],
                                  fg=self.background[2], width=20,
                                  command=lambda: self.verify_user())
        self.sing_in_button.grid(column=2, row=7, padx=20, pady=20, columnspan=3, sticky=tk.EW)


        # base = tk.Label(self.main_frame, width=40, height=20, highlightthickness=10, highlightbackground="black")
        # base.place(x=155, y=200)


class PlaceholderEntry(ttk.Entry):
    '''
    Custom modern Placeholder Entry box, takes positional argument master and placeholder along with\n
    textcolor(default being black) and placeholdercolor(default being grey).\n
    Use acquire() for getting output from entry widget\n
    Use shove() for inserting into entry widget\n
    Use remove() for deleting from entry widget\n
    Use length() for getting the length of text in the widget\n
    BUG 1: Possible bugs with binding to this class\n
    BUG 2: Anomalous behaviour with config or configure method
    '''
    def __init__(self, master, placeholder,textcolor='#606060',placeholdercolor='#606060', password=True, **kwargs):
        self.text = placeholder
        self.__has_placeholder = False # placeholder flag
        self.placeholdercolor = placeholdercolor
        self.textcolor = textcolor
        self.password = password
        self.ch = "*"
        # style for ttk widget
        self.s = ttk.Style()

        # init entry box
        ttk.Entry.__init__(self, master, style='my.TEntry', **kwargs)
        self.s.configure('my.TEntry', forground=self.placeholdercolor)

        # add placeholder if box empty
        self._add()

        # bindings of the widget
        self.bind('<FocusIn>', self._clear)
        self.bind('<FocusOut>', self._add)
        self.bind_all('<Key>', self._normal)
        self.bind_all('<Button-1>', self._cursor)

    def _clear(self, *args): # method to remove the placeholder
        if self.get() == self.text and self.__has_placeholder:  # remove placeholder when focus gain
            if not self.password:
                self.configure(show=self.ch)
            self.delete(0, tk.END)
            self.s.configure('my.TEntry', foreground='#606060',
                             font=(0, 0, 'normal'))
            self.__has_placeholder = False #set flag to false

    def _add(self, *args): # method to add placeholder
        if self.get() == '' and not self.__has_placeholder:  # if no text add placeholder
            if not self.password:
                self.configure(show="")
            self.s.configure('my.TEntry', foreground=self.placeholdercolor,
                             font=(0, 0, 'bold'))
            self.insert(0, self.text)  # insert placeholder
            self.icursor(0)  # move insertion cursor to start of entrybox
            self.__has_placeholder = True #set flag to true

    def _normal(self, *args): #method to set the text to normal properties
        self._add()  # if empty add placeholder
        if self.get() == self.text and self.__has_placeholder:  # clear the placeholder if starts typing
            self.bind('<Key>', self._clear)
            self.icursor(-1)  # keep insertion cursor to the end
        else:
            self.s.configure('my.TEntry', foreground=self.textcolor,
                         font=(0, 0, 'normal'))  # set normal font

    def acquire(self):
        """Custom method to get the text"""
        if self.get() == self.text and self.__has_placeholder:
            return 'None'
        else:
            return self.get()

    def shove(self, index, string):
        """Custom method to insert text into entry"""
        self._clear()
        self.insert(index, string)

    def remove(self, first, last):
        """Custom method to remove text from entry"""
        if self.get() != self.text:
            self.delete(first, last)
            self._add()
        elif self.acquire() == self.text and not self.__has_placeholder:
            self.delete(first, last)
            self._add()

    def length(self):
        """Custom method to get the length of text in the entry widget"""
        if self.get() == self.text and self.__has_placeholder:
            return 0
        else:
            return len(self.get())

    def _cursor(self, *args):  # method to not allow user to move cursor when placeholder exists
        try:
            if self.get() == self.text and self.__has_placeholder:
                self.icursor(0)
        except Exception:
            print("you can't enter text there")

    def toggle(self):

        if self.get() == "Password" and self.ch == "":
            print("bitch")
            self.ch = "*"
            print(self.ch)

        elif self.get() == "Confirm password" and self.ch == "":
            print("bitch")
            self.ch = "*"

        elif self.ch == "*" or self.get() == "Password" or self.get() == "Confirm password":
            self.ch = ""
            self.config(show='')
        else:
            self.ch = "*"
            self.config(show='*')



Interface(["#74DE85", "#1264E3", "#FFFFFF"])
