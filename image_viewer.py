import os
from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("Image Viewer")
root.geometry("600x520")
root.resizable(True, True)


img_dir = "images"

if not os.path.exists(img_dir):
    Label(root, text="Images folder not found").pack(pady=20)
    root.mainloop()
    exit()

img_files = [f for f in os.listdir(img_dir)
             if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]

if not img_files:
    Label(root, text="No images found in folder").pack(pady=20)
    root.mainloop()
    exit()

img_index = 0


def show_image(index):
    global photo
    img_path = os.path.join(img_dir, img_files[index])

    img = Image.open(img_path)
    img.thumbnail((500, 400))   
    photo = ImageTk.PhotoImage(img)

    img_label.config(image=photo)
    img_label.image = photo
    count_label.config(text=f"Image {index + 1} of {len(img_files)}")


def next_image():
    global img_index
    img_index = (img_index + 1) % len(img_files)
    show_image(img_index)

def prev_image():
    global img_index
    img_index = (img_index - 1) % len(img_files)
    show_image(img_index)


img_label = Label(root)
img_label.pack(pady=10)

count_label = Label(root, text="")
count_label.pack()

btn_frame = Frame(root)
btn_frame.pack(pady=10)

Button(btn_frame, text="Previous", width=10, command=prev_image).grid(row=0, column=0, padx=10)
Button(btn_frame, text="Next", width=10, command=next_image).grid(row=0, column=1, padx=10)
Button(btn_frame, text="Exit", width=10, command=root.quit).grid(row=0, column=2, padx=10)

show_image(img_index)
root.mainloop()
