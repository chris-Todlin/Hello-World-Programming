""" 
    Trial case for the GUI
"""

import tkinter as tk
from tkinter import ttk

# 1. INITIALIZE THE MAIN WINDOW
root = tk.Tk()
root.title("My Tkinter Learning Notebook")
root.geometry("400x200") # Width x Height

# 2. DEFINE EVENT FUNCTIONS
def button_was_clicked():
    # Update the text label dynamically
    text_label.config(text="Success! You've triggered a Tkinter event!")
    action_button.config(state="disabled")

# 3. ADD WIDGETS USING THE MODERN 'TTK' THEME
text_label = ttk.Label(root, text="Hello! Press the button below.", font=("Arial", 11))
text_label.pack(pady=20) # 'pack' acts as the vertical layout manager

action_button = ttk.Button(root, text="Click Me!", command=button_was_clicked)
action_button.pack(pady=10)

# 4. START THE WINDOW EVENT LOOP
root.mainloop()
