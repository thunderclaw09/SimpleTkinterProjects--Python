#Weight on mars is 38% of person's weight on earth.
from tkinter import *
from tkinter import ttk
class MyGUI:
    def __init__(self):
        self.root = Tk()
        self.frm = ttk.Frame(self.root, padding=40)
        self.frm.grid()

        self.Answer = ttk.Label(self.frm, text=" ")
        self.Answer.grid(column=0, row=5)
        self.InputNum = ttk.Entry(self.frm, width=40)
        self.InputNum.grid(row=2)

        self.label1 = ttk.Label(self.frm, text="Please input your weight on earth, and the").grid(column=0, row=0)
        self.label2 = ttk.Label(self.frm, text="program will tell you your weight on Mars.").grid(column=0, row=1)
        
        self.Close = ttk.Button(self.frm, text="Quit", command=self.root.destroy).grid(column=3, row=5)
        self.Enter = ttk.Button(self.frm, text="Enter", command=self.EnterFunction).grid(column=3, row=2)

        mainloop()

        # Output = ""

    def EnterFunction(self):
        #global Output

        print("Enter pressed!")
        Number = int(self.InputNum.get())
        NewNumber = (Number / 100) * 38
        print("Your weight on Mars:", NewNumber)
        #Output = ("Your weight on Mars:", NewNumber)
        Output = str(NewNumber)

        # self.Answer['text'] = "This should work."              DID NOT WORK.
        # self.Answer.config(text="This should work.")           ACTUALLY WORKED!   
        # self.Answer.config(text=Output)                        WORKED, BUT IT LOOKED WEIRD
        self.Answer.config(text="Your weight on Mars: "+Output)  # FINALLY WORKED AND LOOKED NICE!

        print("It should have worked.")


    
    

    

  

myGUI = MyGUI()
