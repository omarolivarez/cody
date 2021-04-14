from tkinter import *
from tkinter.filedialog import askopenfilename
import pandas as pd

def import_csv_data():
    global v
    csv_file_path = askopenfilename()
    print(csv_file_path)
    v.set(csv_file_path)
    #df = pd.read_csv(csv_file_path)

# Create window object
app = Tk()

# Import button
import_text = StringVar()
import_label = Label(app, text = "Import Data", font = ('bold', 14), pady = 20, padx = 20)
import_label.grid(row = 30, column = 10)

import_button = Button(app, text='Select CSV file',command=import_csv_data)
import_button.grid(row=30, column=11)

# this code chunk will create a button to close the entire app
#close_button = Button(app, text='Close',command=app.destroy)
#close_button.grid(row=30, column=15)


app.title("Cody")
app.geometry('1300x700')

# Start the program
app.mainloop()