import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename
import pandas as pd
from tkinter.ttk import Frame, Button, Style, Progressbar
from tkinter import scrolledtext

class Cody(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.path = ""
        self.starting_row = 0
        self.df = 0
        
    def initUI(self):
        rl = 1
        rw = 2
        rl2 = 3
        rw2 = 4
        
        
        # this section sets which columns are the ones that move - weight is what will expand when expanded
        self.pack(fill=BOTH, expand=True)
        self.rowconfigure(5, pad=7)
        self.rowconfigure(16, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        
        #lbl = Label(self, text="Windows")
        #lbl.grid(sticky=W, pady=4, padx=5)
        select_btn = Button(self, text="Select CSV",command=self.import_csv_data, width=25)
        select_btn.grid(sticky=E, pady=8, padx=15, columnspan = 1, rowspan=1) 
        
        save_btn = Button(self, text="Save file", command = self.save, width=25)
        save_btn.grid(row=0, column=20, pady = 5, padx = 5, sticky=E)
        
        # white text area
        #area = Text(self)
        #area.grid(row=1, column=0, columnspan=3, rowspan=4, padx=5, sticky=N+S+E+W) 
        self.text_area = scrolledtext.ScrolledText(self, wrap = tkinter.WORD, 
                                      width = 40, padx = 2, height = 10, # padx here is applied internally as a buffer within the text area
                                      font = ("Times New Roman", 13))
        #text_area.insert(INSERT, "")
        self.text_area.grid(row = 1, column = 0, columnspan=3, rowspan=16, pady = 10, padx = 15, sticky=N+S+E+W)
        
        # input fields
        #s2 = Label(self, text = "Placeholder")
        #s2.grid(row = 6, column = 10, padx = 5)
        sl = Label(self, text = "Sex")
        sl.grid(row = rl, column = 20, padx = 8,sticky=W) # 
        self.s = Entry(self)
        self.s.grid(row=rw, column=20, padx = 5, sticky=N+W)
        
        race_l = Label(self, text = "Race")
        race_l.grid(row = 3, column = 20, padx = 8, sticky=W)
        self.race = Entry(self)
        self.race.grid(row=4, column=20, padx = 5, sticky=N+W)
        
        age_l = Label(self, text = "Age")
        age_l.grid(row = 5, column = 20, padx = 8, sticky=W)
        self.age = Entry(self)
        self.age.grid(row=6, column=20, padx = 5, sticky=N+W)
        
        region_l = Label(self, text = "Region of Origin")
        region_l.grid(row = 7, column = 20, padx = 8, sticky=W)
        self.region = Entry(self)
        self.region.grid(row=8, column=20, padx = 5, sticky=N+W)
        
        blm_l = Label(self, text = "BLM Reference")
        blm_l.grid(row = 9, column = 20, padx = 8, sticky=W)
        self.blm = Entry(self)
        self.blm.grid(row=10, column=20, padx = 5, sticky=N+W)
        
        viewpoint_l = Label(self, text = "Viewpoint")
        viewpoint_l.grid(row = 11, column = 20, padx = 8, sticky=W)
        self.viewpoint = Entry(self)
        self.viewpoint.grid(row=12, column=20, padx = 5, sticky=N+W)
        
        style_l = Label(self, text = "Language Style", height = 2)
        style_l.grid(row = 13, column = 20, padx = 8, sticky=W)
        self.style = Entry(self)
        self.style.grid(row=14, column=20, padx = 5, sticky=N+W)
        
        next_btn = Button(self, text="Next row", command=self.next_row, width=16)
        next_btn.grid(row=15, column=20, pady = 20, padx = 5, sticky=N+W)
        
        self.progress = Progressbar(self, orient = HORIZONTAL, length = 100, mode = 'determinate')
        self.progress.grid(row=17, column = 0, columnspan=3, pady = 3, padx = 15, sticky=N+S+E+W)
        
        
       
        
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
        d = pd.read_csv(self.getPath())
        self.setDataframe(d)
        #df = pd.read_csv(self.getPath())
        self.setStartingRow(pd.isnull(self.df).any(1).nonzero()[0][0])
        #starting_row = pd.isnull(df).any(1).nonzero()[0][0]
        #print(starting_row)
        #print(len(df))
        #starting_row = df["Sex"].last_valid_index() + 1
        
        if self.starting_row < len(self.df):
            comment = self.df.iloc[self.starting_row]['User Comment']
            comment = comment.replace("___", "\n\n")
            self.text_area.insert(INSERT, comment)  
            self.progress['value'] = (self.starting_row / len(self.df)) * 100
            self.update_idletasks()
        else:
            self.text_area.insert(INSERT, "CONGRATULATIONS, YOU'RE DONE! \n THIS DATASET HAS BEEN FULLY CODED. ") 
        
    def next_row(self):
        if len(self.s.get())==0 or len(self.race.get())==0 or len(self.age.get())==0 or len(self.region.get())==0 or len(self.blm.get())==0 or len(self.viewpoint.get())==0 or len(self.style.get())==0:
            print("Oh, you left something empty!")
        else:
            # setting sex
            self.df.iat[self.starting_row,1] = int(self.s.get())
            # setting race
            self.df.iat[self.starting_row,2] = int(self.race.get())
            # setting age
            self.df.iat[self.starting_row,3] = int(self.age.get())
            # setting region
            self.df.iat[self.starting_row,4] = int(self.region.get())
            # setting blm reference
            self.df.iat[self.starting_row,5] = int(self.blm.get())
            # setting viewpoint
            self.df.iat[self.starting_row,6] = int(self.viewpoint.get())
            # setting style
            self.df.iat[self.starting_row,7] = int(self.style.get())
            
            self.s.delete(0, END)
            self.race.delete(0, END)
            self.age.delete(0, END)
            self.region.delete(0, END)
            self.blm.delete(0, END)
            self.viewpoint.delete(0, END)
            self.style.delete(0, END)
            
            # adjust text_area
            self.text_area.delete("1.0", "end")
            new_row = self.starting_row + 1
            self.setStartingRow(new_row)
            if self.starting_row <= len(self.df):
                comment = self.df.iloc[self.starting_row]['User Comment']
                comment = comment.replace("___", "\n\n")
                self.text_area.insert(INSERT, comment)  
                self.progress['value'] = (self.starting_row / len(self.df)) * 100
                self.update_idletasks()
            else:
                self.progress['value'] = (self.starting_row / len(self.df)) * 100
                self.update_idletasks()
                self.text_area.insert(INSERT, "CONGRATULATIONS, YOU'RE DONE! \n THIS DATASET HAS BEEN FULLY CODED. ")
        
        
    def save(self):
        #save_path = self.getPath() + "/updated/"
        self.df.to_csv(r'updated.csv', index = False)
        
    def setPath(self, p):
        self.path = p
        
    def getPath(self):
        return self.path
    
    def setStartingRow(self, row):
        self.starting_row = row
        
    def getStartingRow(self):
        return self.starting_row
    
    def setDataframe(self, dataframe):
        self.df = dataframe
        
    def getDataframe(self):
        return self.df

def main():
    global v
    # Create window object
    root = Tk()
    root.title("Cody")
    root.geometry('1200x700') # width x height
    app = Cody()
    root.mainloop()

if __name__ == '__main__':
    main()