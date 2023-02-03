import tkinter as tk
from PIL import ImageTk
from PIL import Image
import os

continue_1 = 1

class SimpleApp(object):
    def __init__(self, master, filename, **kwargs):
        self.master = master
        self.filename = filename
        self.canvas = tk.Canvas(master, width=500, height=500, bg="white")
        self.canvas.pack()

        self.update = self.draw().__next__
        master.after(10, self.update)

    def draw(self):
        global continue_1
        image = Image.open(self.filename)
        angle = 0
        if continue_1 == 1:
            while True:

                tkimage = ImageTk.PhotoImage(image.rotate(angle))
                canvas_obj = self.canvas.create_image(
                    250, 250, image=tkimage)
                self.master.after_idle(self.update)
                yield
                self.canvas.delete(canvas_obj)
                angle += 1.3
                print(angle)
                angle %= 360
                print(angle)
                if int(angle) >= 360:
                    print("stop")
                    continue_1 = 0
                    break

os.chdir("photos")

root = tk.Tk()
root.configure(bg="white")
app = SimpleApp(root, 'log_in_check.png')
root.mainloop()