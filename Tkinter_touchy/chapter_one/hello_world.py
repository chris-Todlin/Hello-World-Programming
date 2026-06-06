""" 
    This is the first prayer to our programming Mother, to bless thy son in try out tkinter
"""
import tkinter as tk
import tkinter.messagebox as msgbox # adding the information

# not the window class
class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Tkinter")
        
        self.label = tk.Label(self, text="Choose one")
        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=30)
        
        # adding the entry part of teh program
        self.name_entry = tk.Entry(self, textvariable="My name is: ")
        self.name_entry.pack(fill=tk.BOTH, expand=1, padx=20, pady=20)
        
        # addint eh button
        hello_button = tk.Button(self, text="Say Hello", command=self.say_hello)
        hello_button.pack(side=tk.LEFT, padx=(20,0), pady=(0,20))
        
        # goodbye Button
        goodbye_button = tk.Button(self, text="Say Goodbye", command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT, padx=(0,20), pady=(0,20))
    
    def say_hello(self):
        msgbox.showerror("Hello", "Hello, there " + self.name_entry.get())
        self.name_entry.configure = ""
    
    def say_goodbye(self):
            # modifying this to ask questions on this
            if msgbox.askquestion("Close Window?","Would you like to close this window?") == 'yes':
                self.label.configure = "Window will close in 2 seconds"
                # msgbox.showwarning("Goodbye!", "Goodbye! \n (Closing in 2 seconds)")
                self.after(2000, self.destroy)
            else:
                msgbox.showinfo("Not CLosing", "Great! This window will stay open")
    
        
# initialte the program
if __name__ == "__main__":
    window = Window()
    window.mainloop()