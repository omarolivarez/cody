import tkinter
from tkinter import *
from tkinter import font
#from tkFileDialog import *
from tkinter.filedialog import askopenfilename
import pandas as pd
from tkinter.ttk import Frame, Button, Style, Progressbar
from tkinter import scrolledtext
import os
import datetime

class Cody(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.path = ""
        self.starting_row = 0
        self.df = 0
        
    def initUI(self):        
        # this section sets which columns are the ones that move - weight is what will expand when expanded
        self.pack(fill=BOTH, expand=True)
        self.rowconfigure(5, pad=7)
        self.rowconfigure(17, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(3, pad=7)
        
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Import csv", command=self.import_csv_data)
        filemenu.add_separator()
        filemenu.add_command(label="Save", command=self.save)
        menubar.add_cascade(label="File", menu=filemenu)

        #select_btn = Button(self, text="Select CSV",command=self.import_csv_data, width=20)
        #select_btn.grid(sticky=W, pady=8, padx=(14, 5), columnspan = 1, rowspan=1, column=0) 
        #save_btn = Button(self, text="Save file", command = self.save, width=18)
        #save_btn.grid(row=0, column=20, pady = 5, padx = 5)
        
        # font size selection widget
        #font_l = Label(self, text = "Font")
        #font_l.grid(row = 1, column = 20, padx = 1,sticky=E)
        
        FONT_OPTS= ["Font Size","11", "12", "13", "14", "16", "18"]
        self.font_var = StringVar(self)
        self.font_var.set(FONT_OPTS[0]) # default value
        dropdown = OptionMenu(self, self.font_var, *FONT_OPTS, command=lambda _: self.getFont())
        dropdown.grid(row = 1, column=20, sticky=E, padx=(2, 15)) 
        
        self.myFont = font.Font(family="Times New Roman", size=13)
        self.text_area = scrolledtext.ScrolledText(self, wrap = tkinter.WORD, width = 40, padx = 2, height = 10, font = self.myFont)
        # padx here is a internal buffer
        
        #text_area.insert(INSERT, "")
        self.text_area.grid(row = 1, column = 0, columnspan=5, rowspan=18, pady = 10, padx = 15, sticky=N+S+E+W)
        
        # input fields
        sl = Label(self, text = "Sex")
        sl.grid(row = 2, column = 19, padx = 0,sticky=E, pady=(70, 0)) 
        self.s = Entry(self)
        self.s.grid(row=2, column=20, padx = (2, 15), sticky=W, pady=(70, 0), columnspan=2)
        
        race_l = Label(self, text = "Race")
        race_l.grid(row = 3, column = 19, padx = 0, sticky=E, pady=(30, 0))
        self.race = Entry(self)
        self.race.grid(row=3, column=20, padx =  (2, 15), sticky=W, pady=(30, 0), columnspan=2)
        
        age_l = Label(self, text = "Age")
        age_l.grid(row = 4, column = 19, padx = 0, sticky=E, pady=(30, 0))
        self.age = Entry(self)
        self.age.grid(row=4, column=20, padx =  (2, 15), sticky=W, pady=(30, 0), columnspan=2)
        
        region_l = Label(self, text = "Region of Origin")
        region_l.grid(row = 5, column = 19, padx = 0, sticky=E, pady=(30, 0))
        self.region = Entry(self)
        self.region.grid(row=5, column=20, padx = (2, 15), sticky=W, pady=(30, 0), columnspan=2)
        
        blm_l = Label(self, text = "BLM Reference")
        blm_l.grid(row = 6, column = 19, padx = 0, sticky=E, pady=(30, 0))
        self.blm = Entry(self)
        self.blm.grid(row=6, column=20, padx = (2, 15), sticky=W, pady=(30, 0), columnspan=2)
        
        viewpoint_l = Label(self, text = "Viewpoint")
        viewpoint_l.grid(row = 7, column = 19, padx = 0, sticky=E, pady=(30, 0))
        self.viewpoint = Entry(self)
        self.viewpoint.grid(row=7, column=20, padx = (2, 15), sticky=W, pady=(30, 0), columnspan=2)
        
        style_l = Label(self, text = "Language Style")
        style_l.grid(row = 8, column = 19, padx = 0, sticky=E, pady=(30, 20))
        self.style = Entry(self)
        self.style.grid(row=8, column=20, padx = (2, 15), sticky=W, pady=(30, 20), columnspan=2)
        
        next_btn = Button(self, text="Next row", command=self.next_row, width=11)
        next_btn.grid(row=9, column=20, padx = (2, 15), sticky=E)
        
        self.labeltext_empty=StringVar()
        self.labeltext_empty.set("")
        self.empty_message = Label(self, justify=LEFT, textvariable=self.labeltext_empty)
        self.empty_message.config(fg="Red")
        self.empty_message.grid(row = 10, column = 20, 
                                padx = (2, 15), pady = (15, 0),sticky=W)
        #self.empty_message = Label(self, text = "",)

        self.progress = Progressbar(self, orient = HORIZONTAL, length = 100, mode = 'determinate')
        self.progress.grid(row=19, column = 0, columnspan=5, pady = 3, padx = 15, sticky=N+S+E+W)
        
        # Import button
        #import_label = Label(self, text = "Import Data", font = ('bold', 14), pady = 20, padx = 20)
        #import_label.grid(row = 30, column = 10)
        
        #import_button = Button(self, text='Select CSV file',command=self.import_csv_data)
        #import_button.grid(row=30, column=11)
        
        # this code chunk will create a button to close the entire app
        #close_button = Button(app, text='Close',command=app.destroy)
        #close_button.grid(row=30, column=15)
        
    def import_csv_data(self):
        csv_file_path = askopenfilename()
        self.setPath(csv_file_path)# .set(csv_file_path)
        d = pd.read_csv(self.getPath())
        self.setDataframe(d)
        print(pd.isnull(self.df).any(1).argmax()) # I AM HERE 
        print()
        # select the row num
        self.setStartingRow(pd.isnull(self.df).any(1).argmax()) # self.setStartingRow(pd.isnull(self.df).any(1).nonzero()[0][0])
        
        if self.starting_row < len(self.df):
            comment = self.df.iloc[self.starting_row]['User Comment']
            # replace the __ with new lines
            comment = comment.replace("___", "\n\n") 
            # add the new comment to the text box
            self.text_area.insert(INSERT, comment)  
            # update the progress bar
            self.progress['value'] = (self.starting_row / len(self.df)) * 100 
            self.update_idletasks()
        else:
            self.text_area.insert(INSERT, "CONGRATULATIONS, YOU'RE DONE! \n THIS DATASET HAS BEEN FULLY CODED. ") 
        
    def next_row(self):
        if len(self.s.get())==0 or len(self.race.get())==0 or len(self.age.get())==0 or len(self.region.get())==0 or len(self.blm.get())==0 or len(self.viewpoint.get())==0 or len(self.style.get())==0:
            self.labeltext_empty.set("One of your entries\nwas left empty.")
            self.master.update()
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
            
            self.labeltext_empty.set("")
            self.master.update()
            
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
        dir_name = filedialog.askdirectory() #tkFileDialog.
        new_folder = "Updated_Coding"
        path = os.path.join(dir_name, new_folder)
        mode = 0o666
        os.mkdir(path, mode)
        today = datetime.date.today().strftime("%Y%m%d")
        filename = "%s_%s.%s" % ("Updated_Coding", today ,"csv")
        filename = os.path.join(path,filename)
        print(filename)
        self.df.to_csv(filename)
        #self.df.to_csv(r'updated.csv', index = False)
        
    def getFont(self):
        font_size = self.font_var.get()
        if font_size.isdecimal():
            self.myFont.configure(size=int(font_size))
        else:
            self.myFont.configure(size=13)
        
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
    root.geometry('1250x700') # width x height
    root.minsize("700", "650")
    app = Cody()
    root.mainloop()

if __name__ == '__main__':
    main()