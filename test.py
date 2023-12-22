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

    # Enable the navigation menu after opening an image
    operations_menu.entryconfig("Operations", state="normal")

def perform_operation(operation_name):
    print(f"Selected Operation: {operation_name}")
    # Add your implementation for each operation here
    # You can perform specific operations based on the selected operation

def save_image():
    # Implement the code to save the image
    pass

def convert_image():
    # Implement the code to convert the image
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
ThemedStyle(root).set_theme("equilux")  # Use a different theme, e.g., "equilux"

# Customize the style for the button
style = ttk.Style()

# Set padding for the menu items
style.layout('TMenubutton', [
   ('Menubutton.border', {'sticky': 'nswe', 'children':
   [('Menubutton.padding', {'sticky': 'nswe', 'children':
   [('Menubutton.label', {'sticky': 'nswe'})]
   })]
   })]
)

# Create a label with project title
project_title = tk.Label(root, text="Image Processing Project", font=('Helvetica', 20, 'bold'), bg=root.cget('bg'), fg='white')
project_title.pack(pady=10)

# Create a button to open a file dialog with the chosen theme
open_button = ttk.Button(root, text="Open Image", command=open_file, style="TButton")
open_button.pack(pady=10)

# Create a label to display the image
image_label = ttk.Label(root)
image_label.pack()

# Create a label with a transparent background to display image details in one line
image_details = tk.Label(root, text="", font=('Helvetica', 12), bg=root.cget('bg'))
image_details.pack(pady=10)

# Create a horizontal menu for operations with the chosen theme
operations_menu = tk.Menu(root, tearoff=0, bg='white', font=('Helvetica', 14, 'bold'))
root.config(menu=operations_menu)

# Add a title to the menu
operations_menu.add_command(label="Operations", state="disabled", foreground='black')

# Add operations to the menu
operations = ["Resize and Scale", "Convert to Gray", "Convert to Binary", "Add Two Images",
              "Draw Hist", "Blinding mode", "Change Contrast", "Contrast Stretching",
              "Blur", "Gaussian Blur", "Image Reflection", "Image Rotation", "Gamma Correction"]

for operation in operations:
    operations_menu.add_command(label=operation, command=lambda op=operation: perform_operation(op), foreground='black', compound=tk.LEFT)

# Create buttons for saving and converting
save_button = ttk.Button(root, text="Save Image", command=save_image, style="TButton")
save_button.pack(pady=10)

convert_button = ttk.Button(root, text="Convert Image", command=convert_image, style="TButton")
convert_button.pack(pady=10)

# Create a button to close the app
close_button = ttk.Button(root, text="Close", command=root.destroy, style="TButton")
close_button.pack(pady=10)

# Bind the event for hovering over menu items
operations_menu.bind("<Enter>", lambda e: e.widget.config(bg='#776472', cursor='hand2'))
operations_menu.bind("<Leave>", lambda e: e.widget.config(bg='white', cursor='arrow'))

# Run the Tkinter event loop
root.mainloop()
