from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
# -------------------------
# Window setup
# -------------------------
root = Tk()
root.title('CCSU App')
root.geometry("500x500")
root.resizable(0, 0)
root.configure(bg='light blue')
# -------------------------
# Make white in logo transparent and show it
# -------------------------

# Pillow>=10 changed ANTIALIAS; this keeps it compatible
img=Image.open("logo.png")
try:
    img = img.resize((100, 100), Image.Resampling.LANCZOS)
except AttributeError:
    img = img.resize((100, 100), Image.ANTIALIAS)
img = img.convert("RGBA")
data = img.getdata()
newData = []
for item in data:
    #if pixel is white make it transparent; else keep it
    if item[:3] == (255, 255, 255):
            newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save("transparent.png")
logo = Image.open("transparent.png")
logo = ImageTk.PhotoImage(logo)
logoLabel = Label(root, image=logo, bg='light blue')
logoLabel.place(x=1, y=1)
# -------------------------
data = pd.read_csv("midterm_exam.csv")
# Label used to display results
lb = Label(root, justify="left", bg="light blue", anchor="w")
lb.place(x=130, y=150)
# -------------------------
# button 1: calendar
def calender():
    df = pd.DataFrame(data, columns=['CalendarDate'])
    selected_rows = df[~df['CalendarDate'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=130, y=150)
# button 2: buildings
def building():
    df = pd.DataFrame(data, columns=['Buildings'])
    selected_rows = df[~df['Buildings'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=130, y=150)
# button 3: faculty
def faculty():
    df = pd.DataFrame(data, columns=['FacultyName'])
    selected_rows = df[~df['FacultyName'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=130, y=150)

button1 = Button(root, text='Calender', command=calender, bg="light green")
button1.place(x=50, y=110)
button2 = Button(root, text='Buildings', command=building, bg="light green")
button2.place(x=150, y=110)
button3 = Button(root, text='Faculty', command=faculty, bg="light green")
button3.place(x=250, y=110)
mainloop()