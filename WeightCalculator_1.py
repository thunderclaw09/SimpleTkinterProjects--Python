#Weight on mars is 38% of person's weight on earth.
from tkinter import *
from tkinter import ttk
class MyGUI:
    def __init__(self):
        self.root = Tk()
        self.frm = ttk.Frame(self.root, padding=40)
        self.frm.grid()

        self.InputNum = ttk.Entry(self.frm, width=40)
        self.InputNum.grid(row=2)

        self.label1 = ttk.Label(self.frm, text="Please input your weight on earth, and the").grid(column=0, row=0)
        self.label2 = ttk.Label(self.frm, text="program will tell you your weight on Mars.").grid(column=0, row=1)
        self.Answer = ttk.Label(self.frm, text="").grid(column=0, row=5)
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
        Output = "Your weight on Mars:", NewNumber
        self.Answer["text"] = "This should work."
        print("It should have worked.")

    
    

    

  

myGUI = MyGUI()




#########################################################################################
#########################################################################################
######   Tadam: this was my original code, when it was not included in a class:    ######
#########################################################################################
#########################################################################################

# root = Tk()
# frm = ttk.Frame(root, padding=40)
# frm.grid()

# InputNum = ttk.Entry(frm, width=40)
# InputNum.grid(row=2)

# # Output = ""

# def EnterFunction():
#     global Output
#     print("Enter pressed!")
#     Number = int(InputNum.get())
#     NewNumber = (Number / 100) * 38
#     print("Your weight on Mars:", NewNumber)
#     # Output = "Your weight on Mars:", NewNumber
#     Answer.config(text="This should work.")
#     print("It should have worked.")

    
# ttk.Label(frm, text="Please input your weight on earth, and the").grid(column=0, row=0)
# ttk.Label(frm, text="program will tell you your weight on Mars.").grid(column=0, row=1)
# Answer = ttk.Label(frm, text="").grid(column=0, row=5)
# Close = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=5)
# Enter = ttk.Button(frm, text="Enter", command=EnterFunction).grid(column=3, row=2)



# root.mainloop()