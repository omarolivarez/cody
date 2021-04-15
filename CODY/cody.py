import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename
import pandas as pd
from tkinter.ttk import Frame, Button, Style
from tkinter import scrolledtext

class Cody(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.path = ""
        
    def initUI(self):
        rl = 1
        rw = 2
        rl2 = 3
        rw2 = 4
        
        
        # this section sets which columns are the ones that move - weight is what will expand when expanded
        self.pack(fill=BOTH, expand=True)
        self.rowconfigure(5, pad=7)
        self.rowconfigure(6, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        
        #lbl = Label(self, text="Windows")
        #lbl.grid(sticky=W, pady=4, padx=5)
        select_btn = Button(self, text="Select CSV",command=self.import_csv_data, width=30)
        select_btn.grid(sticky=E, pady=12, padx=5, columnspan = 10, rowspan=1) #
        
        # white text area
        #area = Text(self)
        #area.grid(row=1, column=0, columnspan=3, rowspan=4, padx=5, sticky=N+S+E+W) 
        self.text_area = scrolledtext.ScrolledText(self, wrap = tkinter.WORD, 
                                      width = 40, padx = 2, height = 10, 
                                      font = ("Times New Roman", 12))
        #text_area.insert(INSERT, "")
        self.text_area.grid(row = 1, column = 0, columnspan=3, rowspan=6, pady = 10, padx = 10, sticky=N+S+E+W)
        
        # input fields
        #s2 = Label(self, text = "Placeholder")
        #s2.grid(row = 6, column = 10, padx = 5)
        sl = Label(self, text = "Sex", height = 2)
        sl.grid(row = rl, column = 10, padx = 5) # 
        self.s = Entry(self)
        self.s.grid(row=rw, column=10, padx = 5)
        
        race_l = Label(self, text = "Race")
        race_l.grid(row = rl, column = 20, padx = 5)
        self.race = Entry(self)
        self.race.grid(row=rw, column=20, padx = 5)
        
        age_l = Label(self, text = "Age")
        age_l.grid(row = rl, column = 30, padx = 5)
        self.age = Entry(self)
        self.age.grid(row=rw, column=30, padx = 5)
        
        region_l = Label(self, text = "Region of Origin")
        region_l.grid(row = rl, column = 40, padx = 5)
        self.region = Entry(self)
        self.region.grid(row=rw, column=40, padx = 5)
        
        blm_l = Label(self, text = "BLM Reference")
        blm_l.grid(row = rl2, column = 10, padx = 5)
        self.blm = Entry(self)
        self.blm.grid(row=rw2, column=10, padx = 5)
        
        viewpoint_l = Label(self, text = "Viewpoint")
        viewpoint_l.grid(row = rl2, column = 20, padx = 5)
        self.viewpoint = Entry(self)
        self.viewpoint.grid(row=rw2, column=20, padx = 5)
        
        style_l = Label(self, text = "Language Style", height = 2)
        style_l.grid(row = rl2, column = 30, padx = 5)
        self.style = Entry(self)
        self.style.grid(row=rw2, column=30, padx = 5, sticky=N)
        
        abtn = Button(self, text="Next row", command=self.clear_text)
        abtn.grid(row=5, column=10, pady = 20, padx = 5, sticky=W)
       
        
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
        #print(csv_file_path)
        self.setPath(csv_file_path)# .set(csv_file_path)
        
        df = pd.read_csv(self.getPath())
        print(df['Sex'])
        print('here')
        starting_row = pd.isnull(df).any(1).nonzero()[0][0]
        print(starting_row)
        print(len(df))
        #starting_row = df["Sex"].last_valid_index() + 1
        
        if starting_row < len(df):
            self.text_area.insert(INSERT, df.iloc[starting_row]['User Comment'])  
        else:
            self.text_area.insert(INSERT, "CONGRATULATIONS, YOU'RE DONE! \n THIS DATASET HAS BEEN FULLY CODED. ") 
        
        
    def clear_text(self):
        self.s.delete(0, END)
        self.race.delete(0, END)
        self.age.delete(0, END)
        self.region.delete(0, END)
        self.blm.delete(0, END)
        self.viewpoint.delete(0, END)
        self.style.delete(0, END)
        
    def setPath(self, p):
        self.path = p
        
    def getPath(self):
        return self.path

def main():
    global v
    # Create window object
    root = Tk()
    root.title("Cody")
    root.geometry('1250x750') # width x height
    app = Cody()
    root.mainloop()

if __name__ == '__main__':
    main()