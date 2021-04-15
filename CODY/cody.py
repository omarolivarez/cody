from tkinter import *
from tkinter.filedialog import askopenfilename
import pandas as pd
from tkinter.ttk import Frame, Button, Style

class Cody(Frame):
    def __init__(self):
        super().__init__()

        self.initUI()
        
    def initUI(self):
        rl = 1
        rw = 2
        
        self.pack(fill=BOTH, expand=True)
        self.rowconfigure(5, pad=7)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        
        #lbl = Label(self, text="Windows")
        #lbl.grid(sticky=W, pady=4, padx=5)
        select_btn = Button(self, text="Select CSV",command=self.import_csv_data)
        select_btn.grid(sticky=W, pady=4, padx=5)
        
        # white text area
        area = Text(self)
        area.grid(row=1, column=0, columnspan=3, rowspan=4, padx=5, sticky=N+S+E+W) 
        
        # input fields
        sl = Label(self, text = "Sex")
        sl.grid(row = rl, column = 10) # 
        s = Entry(self)
        s.grid(row=rw, column=10)
        
        race_l = Label(self, text = "Race")
        race_l.grid(row = rl, column = 20)
        race = Entry(self)
        race.grid(row=rw, column=20)
        
        age_l = Label(self, text = "Age")
        age_l.grid(row = rl, column = 30)
        age = Entry(self)
        age.grid(row=rw, column=30)
        
        region_l = Label(self, text = "Region of Origin")
        region_l.grid(row = rl, column = 40)
        region = Entry(self)
        region.grid(row=rw, column=40)
        
        blm_l = Label(self, text = "BLM Reference")
        blm_l.grid(row = rl, column = 50)
        blm = Entry(self)
        blm.grid(row=rw, column=50)
        
        viewpoint_l = Label(self, text = "Viewpoint")
        viewpoint_l.grid(row = rl, column = 60)
        viewpoint = Entry(self)
        viewpoint.grid(row=rw, column=60)
        
        style_l = Label(self, text = "Language Style")
        style_l.grid(row = rl, column = 70)
        style = Entry(self)
        style.grid(row=rw, column=70)
        
        abtn = Button(self, text="Next row")
        abtn.grid(row=5, column=10)
       
        
        # Import button
        #import_label = Label(self, text = "Import Data", font = ('bold', 14), pady = 20, padx = 20)
        #import_label.grid(row = 30, column = 10)
        
        #import_button = Button(self, text='Select CSV file',command=self.import_csv_data)
        #import_button.grid(row=30, column=11)
        
        # this code chunk will create a button to close the entire app
        #close_button = Button(app, text='Close',command=app.destroy)
        #close_button.grid(row=30, column=15)
        
        ## MAKING THE INPUT FIELDS
        #input fields row number
        
        
    def import_csv_data(self):
        #global v
        csv_file_path = askopenfilename()
        print(csv_file_path)
        #v.set(csv_file_path)
        df = pd.read_csv(csv_file_path)
        #print(head(df))

def main():
    # Create window object
    root = Tk()
    root.title("Cody")
    root.geometry('1350x650')
    app = Cody()
    root.mainloop()

if __name__ == '__main__':
    main()