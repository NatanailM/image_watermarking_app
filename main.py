import time
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

window = tk.Tk()
window.minsize(width=250, height=250)


def open_image():

    def make_watermark():

        txt = Image.new('RGBA', image.size, (255, 255, 255, 0))

        font = ImageFont.truetype('arial.ttf', 36)
        text = watermark_text.get()

        draw = ImageDraw.Draw(txt)

        alpha = 75

        draw.text((float(x.get()), float(y.get())), text, fill=(255, 255, 255, alpha), font=font)
        combined = Image.alpha_composite(image, txt)

        filename = tk.filedialog.asksaveasfilename(defaultextension='.png')

        combined.save(filename)

        image1 = Image.open(filename).convert("RGBA")

        image_tk1 = ImageTk.PhotoImage(image1.resize((800, 480), Image.LANCZOS))

        label.config(image=image_tk1)
        label.image = image_tk1

    filepath = filedialog.askopenfilename()

    if filepath:

        image = Image.open(filepath).convert("RGBA")
        image_tk = ImageTk.PhotoImage(image.resize((800, 480), Image.LANCZOS))

        label.config(image=image_tk)
        label.image = image_tk

        watermark_label = tk.Label(text="Enter the watermark here")
        watermark_label.pack()

        watermark_text = tk.Entry(width=40)
        watermark_text.pack()

        watermark_button = tk.Button(window, text="Watermark Image", command=make_watermark)
        watermark_button.pack(pady=20)

        x_label = tk.Label(window, text="X Coordinate: ")
        x_label.pack()
        x = tk.Entry()
        x.pack(pady=10)
        y_label = tk.Label(window, text="Y Coordinate: ")
        y_label.pack()
        y = tk.Entry()
        y.pack(pady=10)


select_image = tk.Button(window, text="Select Image", command=open_image)
select_image.pack(pady=15)

label = tk.Label(window)
label.pack()

window.mainloop()
