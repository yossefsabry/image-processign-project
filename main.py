import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from ttkthemes import ThemedTk, ThemedStyle
from tkinter import ttk
import os

import cv2

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        display_image(file_path)

def display_image(file_path):
    image = cv2.imread(file_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    image.thumbnail((600, 600))  # Resize the image to fit within a 600x600 pixel box

    tk_image = ImageTk.PhotoImage(image)
    image_label.config(image=tk_image)
    image_label.image = tk_image

    # Display image details in one line
    image_details.config(text=  f"Name: {os.path.basename(file_path)},    "
                                f"Width: {image.width},    "
                                f"Height: {image.height},    "
                                f"Format: {image.format}")

    # Enable the dropdown menu after opening an image
    operations_combobox['state'] = 'readonly'

def perform_operation():
    selected_operation = operations_combobox.get()
    if selected_operation == "Resize and Scale":
        # Implement the code for Resize and Scale operation here
        pass
    elif selected_operation == "Convert to Gray":
        # Implement the code for Convert to Gray operation here
        pass
    elif selected_operation == "Convert to Binary":
        # Implement the code for Convert to Binary operation here
        pass

# Create the main window using ThemedTk
root = ThemedTk(theme="arc")  # Use a theme from ttkthemes
root.title("Image Viewer")

# Change the background color and opacity for the app
root.configure(bg='#776472')
root.attributes('-alpha', 0.95)  # Set opacity (0.0 to 1.0)

# Set the size for the window (width, height)
root.geometry("1000x800")

# Apply the theme to the entire window
ThemedStyle(root).set_theme("arc")

# Customize the style for the button
style = ttk.Style()
style.configure("TButton", background='#776472', borderwidth=0)

# Create a label with project title
project_title = tk.Label(root, text="Image Processing Project", font=('Helvetica', 20, 'bold'), bg=root.cget('bg'), fg='white')
project_title.pack(pady=10)

# Create a button to open a file dialog with Bootstrap style
open_button = ttk.Button(root, text="Open Image", command=open_file, style="TButton")
open_button.pack(pady=10)

# Create a label to display the image
image_label = ttk.Label(root)
image_label.pack()

# Create a label with a transparent background to display image details in one line
image_details = tk.Label(root, text="", font=('Helvetica', 12), bg=root.cget('bg'))
image_details.pack(pady=10)

# Create a regular Label for "Operations" with a transparent background
operations_label = tk.Label(root, text="Operations", font=('Helvetica', 14, 'bold'), bg=root.cget('bg'), fg='white')
operations_label.pack(pady=5)

operations_combobox = ttk.Combobox(root, values=["Resize and Scale", "Convert to Gray", "Convert to Binary", "Add Two Images" , "Draw Hist", "Blinding mode", "Change Contrast", "Contrast Stretching"," Blur ", "Gaussian Blur" , "Image Reflection", "Image Rotation", "Gamma Correction"])
operations_combobox.set("Select Operation")
operations_combobox['state'] = 'disabled'  # Initially disabled until an image is opened
operations_combobox.pack(pady=5)

# Button to perform the selected operation
perform_button = ttk.Button(root, text="Perform Operation", command=perform_operation, style="TButton")
perform_button.pack(pady=10)

# Create a button to close the app
close_button = ttk.Button(root, text="Close", command=root.destroy, style="TButton")
close_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
