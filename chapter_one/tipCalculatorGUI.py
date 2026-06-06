""" 
    This is the Gui Version of the tip calculator with all part in like the one
    implement using the html, css and js
"""

# import the modules
import tkinter as tk
import tkinter.messagebox as msgbox

# the tip calculator clas
class TipCaclulator(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # add the title of the class
        self.title("Tip Caculator") 
        self.geometry("500x300") # set the geomerty of the application
        
        # Add the header wdiget
        self.header = tk.Label(self, text="Tip Caculator", font=("Arial", 20))
        self.header.pack()
        
        # add the label and entry of the bill
        self.bill_label = tk.Label(self, text="Bill Amount: ")
        self.bill_label.pack()
        self.bill_entry = tk.Entry(self, textvariable="Bill Amount: ")
        self.bill_entry.pack()
        
        # add the label and entry of the tip percent
        self.tip_percentage = tk.Label(self, text="Tip Percentage: ")
        self.tip_percentage.pack()
        self.tip_percentage_entry = tk.Entry(self, textvariable="Tip percentage: ")
        self.tip_percentage_entry.pack()
        
        # adding teh button to calculate the tip percentage
        self.tip_button = tk.Button(self, text="Calculate tip", command=self.calculateTip)
        self.tip_button.pack()
        
        # the label for the bill total and the tip amount
        self.tip_total = tk.Label(self, text="Total Tip: $ ")
        self.tip_total.pack()
        self.bill_total = tk.Label(self, text="")
        self.bill_total.pack()
        
    # function to calculate the total tip
    def calculateTip(self):
        try:
            bill = int(self.bill_entry.get())
            tipPercentage = int(self.tip_percentage_entry.get())
            
            # show the message of the tip amount
            # else cacluate the tip 
            tipAmount = bill * (tipPercentage/100)
            totalBill = bill + tipAmount
            
            # display the message
            self.tip_total.config(text="Total Tip: $ " + str(tipAmount))
            self.bill_total.config(text="Total Bill: $ " + str(totalBill))
        except:
            # show an error message
            msgbox.showerror("Invalid input","Check your inputs")
        

# running the application
if __name__ == "__main__":
    tipCalc = TipCaclulator()
    tipCalc.mainloop()