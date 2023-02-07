import tkinter as tk
from PIL import ImageTk
from PIL import Image
import os



class SimpleApp(object):
    def __init__(self, master, filename, **kwargs):
        self.continue_1 = 1
        self.master = master
        self.filename = filename
        self.canvas = tk.Canvas(master, width=500, height=500, bg="white")
        self.canvas.pack()
        if self.continue_1 == 1:
            self.update = self.draw().__next__
            master.after(15, self.update)
            print("ainceput")

    def draw(self):

        image = Image.open(self.filename)
        angle = 0

        while True:



                tkimage = ImageTk.PhotoImage(image.rotate(angle))
                canvas_obj = self.canvas.create_image(
                    250, 250, image=tkimage)
                self.master.after_idle(self.update)
                yield
                self.canvas.delete(canvas_obj)
                print("")
                print("")
                print("")
                print(angle)
                angle += 1.3
                print(angle)
                angle %= 360
                print(angle)


    def end_cycle(self):
        print("boss")

os.chdir("photos")

root = tk.Tk()
root.configure(bg="white")
app = SimpleApp(root, 'log_in_check.png')
root.mainloop()