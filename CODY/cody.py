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
from itertools import compress # for converting true false list into shorter version

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
    
    def nextPopup(self):
        selected = (list(map(lambda x: x.get(), self.a)))
        true_false_list = [x=="categorical" for x in selected]
        # now get just the ones that are true
        categorical_vars = list(compress(self.cats_list, true_false_list))

        # destroy the old window
        self.win.destroy()

        # create new window
        win2 = Toplevel()
        win2.minsize("450", "550") # width x height
        win2.wm_title("Categories")

        # add the categorical variables to the window
        n = 0
        popup2_start = Label(win2, text="Add your categories for each code. Separate each category with a semicolon and a space.\nEach category may include any character, including spaces and hyphens.")
        popup2_start.grid(row=0, column=0, columnspan = 3, pady=(15, 15), padx=(15,0), sticky=W)

        for n in range(len(categorical_vars)): 
                l = Label(win2, text=categorical_vars[n]).grid(row= n+1, column=0, padx=(15, 0), pady=(0, 5), sticky=E)
        return

    def import_csv_data(self):
        csv_file_path = askopenfilename() # open the file manager to select CSV
        self.setPath(csv_file_path)# .set(csv_file_path)
        d = pd.read_csv(self.getPath()) # initialize the dataframe
        self.setDataframe(d)
        # select the row num
        self.setStartingRow(pd.isnull(self.df).any(1).argmax()) # self.setStartingRow(pd.isnull(self.df).any(1).nonzero()[0][0])
        # what this line above does: create a series that sets non-null rows to False and null rows to true. Find the first one (argmax). 
        
        if self.starting_row < len(self.df):
            # create a popup to set variables
            self.win = Toplevel()
            self.win.minsize("550", "450") # width x height
            self.win.wm_title("Annotation scheme")
            popup_start = Label(self.win, text="Identify your codes as either continuous or categorical.")
            popup_start.grid(row=0, column=0, columnspan = 3, pady=(15, 2), padx=(15,0), sticky=W)
            popup_warning_label = Label(self.win, text="(Warning: Avoid importing more than 15 codes)")
            popup_warning_label.grid(row=1, column=0, columnspan = 3, pady=(2, 15), padx=(15,0), sticky=W)

            # get columns
            columns_from_df = d.columns

            # window options setup
            CATEGORY_OPTIONS= ["continuous", "categorical"]
            num_df_cols = len(columns_from_df) # number of columns to iterate over
            # labels to create in the popup
            pop_up_labels = [] 

            # set up the dropdown configs
            dropdown_list = []
            self.categories_selected = []
            #self.category_selected = StringVar(self) can remove these two later
            #self.category_selected.set("Variable type")
            # set up the entry box list
            self.setCategoriesEntry()
            #scrollbars = [] # not needed for now

            self.cats_list = columns_from_df[1:]
            self.a = [StringVar(self.win) for i in range(len(self.cats_list))]
            n = 0
            for n in range(len(self.cats_list)): 
                l = Label(self.win, text=self.cats_list[n]).grid(row= n+2, column=1, padx=(15, 0), pady=(0, 5), sticky=E)
                #Strg_var = StringVar(self.win) # maybe not needed
                self.a[n].set("Variable type")
                o = OptionMenu(self.win, self.a[n], *CATEGORY_OPTIONS)
                o.config(width=10)
                o.grid(row = n+2, column=2, padx=10)

            """
            # loop to create empty optionmenu text holders
            for i in range(1, num_df_cols):
                sr = StringVar(self)
                sr.set("Variable type")
                print(i, "first")
                dropdown_popup = OptionMenu(self.win, sr, *CATEGORY_OPTIONS) #, command=lambda _: self.enableCategoryEntry(i-1)
                print(i, "second")
                dropdown_popup.config(width=10)
                dropdown_popup.grid(row=i+1, column=1, padx=10)
                self.categories_selected.append(dropdown_popup)
            
            # loop to create labels, optionmenus, and entries in pop-up window
            for i in range(1, num_df_cols): # start at 1 to avoid selecting the text column
                # for every column except the first one, create a label and a dropdown with the same values
                pop_up_labels.append(Label(self.win, text=columns_from_df[i]))
                #print(i)
                ###dropdown_list.append(OptionMenu(win, self.categories_selected[i], *CATEGORY_OPTIONS, command=lambda _: self.enableCategoryEntry(i)))
                ###self.categories_entries.append(Text(self.win, height = 3, width = 40, wrap="word"))
                ## these two lines below were the add scrollbars, but are unnecessary
                #scrollbars.append(Scrollbar(win, orient = 'vertical', command = categories_entries[i].yview))
                #categories_entries[i]['yscrollcommand'] = scrollbars[i].set
            
            # loop to add the labels, optionmenus, and entries to the grid
            for i in range(len(pop_up_labels)): # loop over the index of the labels, do this to use this as the col index in grid()
                # first, place the label
                pop_up_labels[i].grid(row=i+2, column=0, padx=(15, 10))
                # now add the dropdown next to each label
                ###dropdown_list[i].config(width=10)
                ###dropdown_list[i].grid(row=i+2, column=1, padx=10)
                # now add the entry boxes
                ###self.categories_entries[i].grid(row=i+2, column=2, padx=(10, 15))
                # now disable the widget:
                ###self.categories_entries[i].config(state=DISABLED)
            """
            b = Button(self.win, text="Done", command=self.nextPopup)
            b.grid(row=len(self.cats_list)+2, column=2, pady=(15, 5), padx=(0, 15))

            ## update the text box with the last not-coded row
            comment = self.df.iloc[self.starting_row]['User Comment']
            # replace the __ with new lines
            comment = comment.replace("___", "\n\n") 
            # add the new comment to the text box
            self.text_area.insert(INSERT, comment)  
            # update the progress bar
            self.progress['value'] = (self.starting_row / len(self.df)) * 100 
            self.update_idletasks()
        else:
            # in this case, the CSV is completed filled out
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

    def enableCategoryEntry(self, index):
        #selection = self.categories_selected
        print('third')
        print(index)
        selection = self.categories_selected[index].get()
        print(selection)
        if selection=="categorical":
            print("INDEX:")
            self.categories_entries[index].config(state=NORMAL) 
        return

    
    
    def setCategoriesEntry(self):
        self.categories_entries = []
        
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