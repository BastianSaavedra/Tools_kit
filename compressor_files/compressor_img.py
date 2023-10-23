# Used libraries
import os, time
from PIL import Image
import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.withdraw()

extension = (("Images Files", "*.jpg *.jpeg *.png"), ("All", "*.*"))

file_path = filedialog.askopenfilename(
        title="Select the image that you want to compress",
        filetypes=extension
        )
file_name = file_path.split('/')[-1]
_index = file_path.rfind('/')
current_path = file_path[:_index + 1] if _index != -1 else print('path not found')
if file_path:
    print("File Selected: ", file_name)
    img = Image.open(current_path + file_name)
    timestamp = int(time.time())
    compresed_name = f"{current_path}compreessed_{str(timestamp)}_{file_name}"
    img.save(compresed_name, optimize=True, quality=60)
    print(f"Compressed complete and saved it at {current_path}")
else:
    print("No file selected")

root.destroy()






