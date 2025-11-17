import tkinter as tk
from tkinter import ttk

class BookPointsApp:
    def __init__(self, root):
        #This will create the window
        self.root = root
        self.root.title('Serendipity Book Points')
        self.root.geometry("380x200")
        #This will create the label for the instructions
        self.instructlbl=ttk.Label(root, text="Enter the amount of books you've purchased this month:")
        self.instructlbl.grid(column=0, row=0)
        #this is the widget for the user entry
        self.bookentry=ttk.Entry(root, width=5)
        self.bookentry.grid(column=1, row=0)
        #This is the button to press for calculating the points
        self.calcbtn=ttk.Button(root,text='Calculate Points', command=self.calcptsdisplay)
        self.calcbtn.grid(column=0, row=2)
        #This is the string var to set the points at 0
        self.points_var=tk.StringVar()
        self.points_var.set('0')
        #This is where the output will be displayed
        outputlbl=ttk.Label(root,text='you have earned:')
        outputlbl.grid(column=0, row=3)
        outputval=tk.Label(root,textvariable=self.points_var)
        outputval.grid(column=1, row=3)
    #This will help to calculate and display the points
    def calcptsdisplay(self):
       try:
            bookspurchased=int(self.bookentry.get())
            points=0
            if bookspurchased < 0:
                self.points_var.set('invalid input')
                return
            if bookspurchased == 0:
                points=0
            elif bookspurchased == 2:
                points=5
            elif bookspurchased == 4:
                points=15
            elif bookspurchased == 6:
                points=30
            elif bookspurchased >= 8:
                points=60
            else:
                points=0
            self.points_var.set(f'{points} points')
       except ValueError:
            self.points_var.set('invalid input')


def main():
    root = tk.Tk()
    app = BookPointsApp(root)
    root.mainloop()
if __name__ == '__main__':
    main()




