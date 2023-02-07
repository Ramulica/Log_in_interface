import tkinter as tk
import sqlite3
import os
from tkinter import ttk as ttk
from PIL import ImageTk
from PIL import Image
from validate_email_address import validate_email
import string
import time


class Interface:
    def __init__(self, background):

        self.background = background



        self.root = tk.Tk()
        self.root.geometry("600x700")
        self.root.configure(bg="black")

        self.main_frame = tk.Frame(self.root)
        self.main_frame.configure(bg=self.background[0])
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        # IMAGES
        self.main_path = os.getcwd()
        os.chdir("photos")
        self.logo_image = tk.PhotoImage(file="Logo_image.png")
        self.check_image_1 = Image.open("log_in_check.png")
        self.check_image = ImageTk.PhotoImage(self.check_image_1)

        self.dgg_button = tk.PhotoImage(file="dark_grey_grey_button.png")
        self.bs_button = tk.PhotoImage(file="bej_skin_button.png")
        self.gb_button = tk.PhotoImage(file="green_blue_button.png")
        self.pm_button = tk.PhotoImage(file="purple_magenta_button.png")
        self.wb_button = tk.PhotoImage(file="white_blue_button.png")
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
                                    command=lambda: self.settings_interface())
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

        self.username_entry = PlaceholderEntry(self.username_frame, placeholder="Email", font=("Arial", 20, "bold"))
        self.username_entry.pack(fill=tk.BOTH, padx=5, pady=5)

        self.password_frame = tk.Frame(self.main_frame, bg=self.background[1])
        self.password_frame.grid(column=2, row=3, padx=20, pady=20, columnspan=3, sticky=tk.EW)

        self.password_entry = PlaceholderEntry(self.password_frame, placeholder="Password", font=("Arial", 20, "bold"),
                                               password=False)
        self.password_entry.pack(fill=tk.BOTH, padx=5, pady=5)

        self.c1 = tk.Checkbutton(self.main_frame, text='Show Password', bg=self.background[0],
                                 command=self.password_entry.toggle)
        self.c1.grid(row=4, column=2, sticky=tk.W, padx=20)

        self.log_in_button = tk.Button(self.main_frame, text="Log In", font=("Arial", 20, "bold"), bg=self.background[1],
                                  fg=self.background[2], width=20,
                                  command=lambda: self.verify_user())
        self.log_in_button.grid(column=2, row=5, padx=20, pady=20, columnspan=3, sticky=tk.EW)



    def sing_in_verification(self):
        self.email_frame.configure(bg=self.background[1])
        self.username_frame.configure(bg=self.background[1])
        self.password_frame.configure(bg=self.background[1])
        self.confirm_password_frame.configure(bg=self.background[1])
        error_message = []
        if not validate_email(self.email_entry.get()):
            print(self.username_entry.get(), "asdasd")
            self.email_frame.configure(bg="red")
            error_message.append("email")
        elif self.email_entry.get() in SQLtable.read_column("email"):
            self.email_frame.configure(bg="red")
            error_message.append("email exists")
        if not self.verify_username():

            self.username_frame.configure(bg="red")
            error_message.append("username")
        if not self.verify_password():
            self.password_frame.configure(bg="red")
            error_message.append("password")
        if not self.verify_password_confirmation():
            self.confirm_password_frame.configure(bg="red")
            error_message.append("password confirmation")
        if len(error_message) == 0:
            print(self.email_entry.get(), self.username_entry.get(), self.password_entry.get())
            data = SQLtable(self.email_entry.get(), self.username_entry.get(), self.password_entry.get())
            data.write_data_in_sql()
            self.log_in_successful_interface("SING IN SUCCESSFUL", 16)
        else:
            self.error_message = tk.Label(self.main_frame, text=f"ERROR: {' '.join(error_message)} are wrong",
                                          font=("Arial", 12, "bold"), fg="red", bg=self.background[0])
            self.error_message.grid(column=2, row=8, padx=20, pady=20, columnspan=3, sticky=tk.EW)
            self.root.after(5000, self.error_message.destroy)

    def verify_user(self):
        self.data = SQLtable.get_data_from_email(self.username_entry.get())
        error_massage = ""
        self.username_frame.configure(bg=self.background[1])
        self.password_frame.configure(bg=self.background[1])

        if type(self.data) == str:
            self.username_frame.configure(bg="red")
            self.password_frame.configure(bg="red")
            self.error_message = tk.Label(self.main_frame, text=f"ERROR:  Email doesn't exist",
                                          font=("Arial", 12, "bold"), fg="red", bg=self.background[0])
            self.error_message.grid(column=2, row=8, padx=20, pady=20, columnspan=3, sticky=tk.EW)
            self.root.after(5000, self.error_message.destroy)
        elif self.password_entry.get() != self.data[2]:
            self.password_frame.configure(bg="red")
            self.error_message = tk.Label(self.main_frame, text=f"ERROR: Incorrect password",
                                          font=("Arial", 12, "bold"), fg="red", bg=self.background[0])
            self.error_message.grid(column=2, row=8, padx=20, pady=20, columnspan=3, sticky=tk.EW)
            self.root.after(5000, self.error_message.destroy)
        else:
            self.log_in_successful_interface("LOG IN SUCCESSFUL", 17)

    def verify_username(self):
        if len(self.username_entry.get()) == 0 or self.username_entry.get() == "Username":
            return False
        for ch in self.username_entry.get():
            if ch in '!"#$%&\'*()+,/:;<=>?@[\\]^`{|}~':
                return False
        else:
            return True

    def verify_password(self):
        if len(self.password_entry.get()) < 8:
            return False
        for ch in self.password_entry.get():
            if self.password_entry.get().count(ch) > 3:
                return False
        ch_letter = 0
        for ch in self.password_entry.get():
            if ch in string.ascii_letters:
                ch_letter += 1
        if ch_letter == len(self.password_entry.get()):
            return False
        return True

    def verify_password_confirmation(self):
        if self.confirm_password_entry.get() == self.password_entry.get():
            return True
        else:
            return False

    def log_in_successful_interface(self, text, font):
        self.make_a_new_frame()


        self.first_label = tk.Label(self.main_frame, background="#8FC642", width=43, height=25,)
        self.first_label.place(x=150, y=150)
        self.first_label = tk.Label(self.main_frame, background="white", width=38, height=23,)
        self.first_label.place(x=167, y=165)

        self.check_lable = tk.Label(self.main_frame, image=self.check_image, borderwidth=0)
        self.check_lable.place(x=225, y=225)

        self.text_label = tk.Label(self.main_frame, text=text, font=("Arial", font, "bold"),
                                   fg="#8FC642", bg="white")
        self.text_label.place(x=180, y=450)

        self.rotate_logo()



    def rotate_logo(self):
        global angle
        self.check_lable.destroy()
        self.check_image = ImageTk.PhotoImage(self.check_image_1.rotate(angle))

        self.check_lable = tk.Label(self.main_frame, image=self.check_image, borderwidth=0)
        self.check_lable.place(x=225, y=225)


        angle += 5
        if angle == 365:
            print("end")
        else:
           self.root.after(5, self.rotate_logo)


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
                                 fg=self.background[2], command=self.password_entry.toggle)
        self.c1.grid(row=4, column=2, sticky=tk.W, padx=20)

        self.confirm_password_frame = tk.Frame(self.main_frame, bg=self.background[1])
        self.confirm_password_frame.grid(column=2, row=5, padx=20, pady=20, columnspan=3, sticky=tk.EW)

        self.confirm_password_entry = PlaceholderEntry(self.confirm_password_frame, placeholder="Confirm password", font=("Arial", 20, "bold"), password=False, show="*")
        self.confirm_password_entry.pack(fill=tk.BOTH, padx=5, pady=5)

        self.c2 = tk.Checkbutton(self.main_frame, text='Show Password Confirmation', bg=self.background[0],
                                 fg=self.background[2], command=self.confirm_password_entry.toggle)
        self.c2.grid(row=6, column=2, sticky=tk.W, padx=20)

        self.sing_in_button = tk.Button(self.main_frame, text="Sing In", font=("Arial", 20, "bold"), bg=self.background[1],
                                  fg=self.background[2], width=20,
                                  command=lambda: self.sing_in_verification())
        self.sing_in_button.grid(column=2, row=7, padx=20, pady=20, columnspan=3, sticky=tk.EW)


        # base = tk.Label(self.main_frame, width=40, height=20, highlightthickness=10, highlightbackground="black")
        # base.place(x=155, y=200)
    def settings_interface(self):
        self.make_a_new_frame()

        self.back_button = tk.Button(self.main_frame, text=" ◀ ", font=("Arial", 15), bg="red",
                                fg=self.background[2],
                                command=lambda: self.main_interface())
        self.back_button.grid(row=0, column=0)

        self.space_label = tk.Label(self.main_frame, bg=self.background[0], text=f"{'X'* 75}", fg=self.background[0])
        self.space_label.grid(row=0, column=2)

        self.color_frame = tk.Frame(self.main_frame, bg=self.background[1])
        self.color_frame.grid(column=2, row=1, padx=20, pady=20, columnspan=3, sticky=tk.EW)

        self.color_title = tk.Label(self.color_frame, text="Choose color team", bg=self.background[1]
                                    , fg=self.background[2], font=("Arial", 25, "bold"))
        self.color_title.grid(row=0, column=0, padx=5, pady=5, columnspan=5)

        self.button_0 = tk.Button(self.color_frame, image=self.gb_button, command=lambda x=0: self.set_background(x)
                                  , fg=self.background[2], borderwidth=0, bg="black")
        self.button_0.grid(row=1, column=0, padx=10, pady=5)
        self.button_1 = tk.Button(self.color_frame, image=self.pm_button, command=lambda x=1: self.set_background(x),
                                  fg=self.background[2], borderwidth=0, bg="black")
        self.button_1.grid(row=1, column=1, padx=10, pady=5)
        self.button_2 = tk.Button(self.color_frame, image=self.bs_button, command=lambda x=2: self.set_background(x),
                                  fg=self.background[2], borderwidth=0, bg="black")
        self.button_2.grid(row=1, column=2, padx=10, pady=5)
        self.button_3 = tk.Button(self.color_frame, image=self.dgg_button, command=lambda x=3: self.set_background(x),
                                  fg=self.background[2], borderwidth=0, bg="black")
        self.button_3.grid(row=1, column=3, padx=10, pady=5)
        self.button_4 = tk.Button(self.color_frame, image=self.wb_button, command=lambda x=4: self.set_background(x),
                                  fg=self.background[2], borderwidth=0, bg="black")
        self.button_4.grid(row=1, column=4, padx=10, pady=5)




    def set_background(self, index):
        list_of_packgrounds = [["#74DE85", "#1264E3", "#FFFFFF"], ["#6E00B6", "#A9008A", "#FFFFFF"],
                               ["#A79B5A", "#DACB76", "#000000"], ["#3F3F3F", "#606060", "#FFFFFF"],
                               ["#CECECE", "#1F5DBB", "#000000"]]
        self.background = list_of_packgrounds[index]
        self.settings_interface()


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


class SQLtable:
    def __init__(self, email, username, password):
        self.email = email
        self.password = password
        self.username = username

    def write_data_in_sql(self):
        con = sqlite3.connect("Users.db")
        cur = con.cursor()
        create_command = f"""CREATE TABLE IF NOT EXISTS user_data(
                            email TEXT,
                            username TEXT,
                            password TEXT,
                            PRIMARY KEY(email)
                            );"""

        cur.execute(create_command)
        try:
            insert_command = f"""INSERT INTO user_data VALUES('{self.email}',
                                                       '{self.username}',
                                                       '{self.password}');"""
            cur.execute(insert_command)
        except sqlite3.Error:
            print(f"error: {self.username} couldn't be added")
        con.commit()

        con.close()

    @staticmethod
    def read_column(column):
        con = sqlite3.connect("Users.db")
        cur = con.cursor()
        try:
            actors = cur.execute(f"SELECT {column} FROM user_data")
            output_1 = actors.fetchall()
            con.commit()
        except sqlite3.Error:
            return tuple(())

        con.close()
        return output_1
    @staticmethod
    def get_data_from_email(email):


        for item in SQLtable.read_column("*"):
            if item[0] == email:
                return item
        else:
            return "Email doesn't exist"


angle = 0



Interface(["#74DE85", "#1264E3", "#FFFFFF"])
