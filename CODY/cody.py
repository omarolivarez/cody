import tkinter
from tkinter import *
from tkinter import font
#from tkFileDialog import *
from tkinter import filedialog # to open dialog to save
from tkinter.filedialog import askopenfilename
import pandas as pd
from tkinter.ttk import Frame, Button, Style, Progressbar
from tkinter import scrolledtext
import os
import datetime
from itertools import compress # for converting true false list into shorter version

# MAKING THIS A GLOBAL VARIABLE SO IT CAN BE ACCESSING IN import_csv()
# Create window object
root = Tk()

class Cody(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.path = ""
        self.starting_row = 0
        self.df = 0
        
    def initUI(self):        
        # this section sets which columns are the ones that move - weight is what will expand when expanded
        #self.pack(fill=BOTH, expand=True) # see if I can add this back later
        self.rowconfigure(5, pad=7)
        self.rowconfigure(17, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(3, pad=7)
        race_l = Label(self, text = "Race")
        race_l.grid(row = 3, column = 19, padx = 0, sticky=E, pady=(30, 0))

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
        """
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
        #close_button.grid(row=30, column=15)"""
    
    """nextPopup() is used to configure the categories for each code that was identified as a categorical variable
       once this step is complete, the user will be taken to the main screen to do their coding"""
    def nextPopup(self):
        # get the OptionMenu selection for each OptionMenu from popup window #1
        selected = (list(map(lambda x: x.get(), self.a)))
        # create a new list where each index where there was a "categorical" in "selected" is TRUE, else FALSE
        true_false_list = [x=="categorical" for x in selected]
        # now get just the ones in "selected" that are true
        categorical_vars = list(compress(self.cats_list, true_false_list))

        # create a dictionary
        self.codes_dict = {}

        # potentially delete this block - not using order at the moment
        order = 0
        # add codes to it as keys
        for code in self.cats_list:
            self.codes_dict[code] = []
            if code in categorical_vars:
                self.codes_dict[code].append(order)
                order += 1
            else:
                self.codes_dict[code].append(order) # pick a value below 0 arbitrarily
                order += 1

        # destroy the old window
        self.win.destroy()

        # create new window
        self.win2 = Toplevel()
        self.win2.minsize("550", "550") # width x height
        self.win2.wm_title("Categories")

        # add the categorical variables to the window
        n = 0
        # add the two labels at the top of the window
        popup2_start = Label(self.win2, text="Add your categories for each code. Separate each category with a semicolon and a space.")
        popup2_start.grid(row=0, column=0, columnspan = 3, pady=(15, 2), padx=(15,15), sticky=W)
        popup2_start2 = Label(self.win2, text="Each category may include any character, including spaces and hyphens.")
        popup2_start2.grid(row=1, column=0, columnspan = 3, pady=(0, 5), padx=(15,15), sticky=W)
        popup2_start3 = Label(self.win2, text="Example: North America; South America; Africa;")
        popup2_start3.grid(row=2, column=0, columnspan = 3, pady=(0, 15), padx=(15,15), sticky=W)

        #self.b = [StringVar(self.win) for i in range(len(self.cats_list))]
        #self.b[n].set("Variable type")
        for n in range(len(categorical_vars)): 
                # add 3 to row because the first 3 rows are taken up by the three labels above
                l = Label(self.win2, text=categorical_vars[n]).grid(row= n+3, column=0, padx=(15, 0), pady=(0, 5), sticky=E) 
                te = Text(self.win2, height = 4, width = 50, wrap="word")
                te.grid(row=n+3, column=1, padx=(5, 15), pady=(0, 5))

                # add Text to dictionary and refernce it's text later
                self.codes_dict[categorical_vars[n]].append(te)

        # get the text from the entries
        #selected = (list(map(lambda x: x.get(), self.a)))

        # create next button that takes you to main screen
        button_popup2 = Button(self.win2, text="Finish", command=self.addCodes) #
        button_popup2.grid(row=len(categorical_vars)+3, column=2, pady=(15, 10), padx=(0, 15), sticky=E)

    def import_csv_data(self):
        csv_file_path = askopenfilename() # open the file manager to select CSV
        #root.iconify() # this hides the old window but keeps it around so the entire app doesn't close
        self.setPath(csv_file_path)# .set(csv_file_path)
        d = pd.read_csv(self.getPath()) # initialize the dataframe
        # convert all columns to string
        lst = list(d)
        d[lst] = d[lst].astype(str)

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

            b = Button(self.win, text="Next", command=self.nextPopup)
            b.grid(row=len(self.cats_list)+2, column=2, pady=(15, 5), padx=(0, 15))

            ## update the text box with the last not-coded row
            #comment = self.df.iloc[self.starting_row]['User Comment']
            ## replace the __ with new lines
            #comment = comment.replace("___", "\n\n") 
            ## add the new comment to the text box
            #self.text_area.insert(INSERT, comment)  
            ## update the progress bar
            #self.progress['value'] = (self.starting_row / len(self.df)) * 100 
            #self.update_idletasks()
        #else:
        #    # in this case, the CSV is completed filled out
        #    self.text_area.insert(INSERT, "CONGRATULATIONS, YOU'RE DONE! \n THIS DATASET HAS BEEN FULLY CODED. ") 
        
    def next_row(self):
        selected_entries = (list(map(lambda x: x.get(), self.b)))
        # turn empty entries into True
        true_false_entries = [x=="" or x=="Select option" for x in selected_entries]
        if True in true_false_entries:
            self.labeltext_empty.set("One of your entries\nwas left empty.")
            self.master.update()
        else:
            # values in the order that they appear
            # get the colnames
            print(selected_entries)
            print("Number of entries:", len(selected_entries))
            for ent in range(len(selected_entries)):
                self.df.iat[self.starting_row, ent+1] = str(selected_entries[ent]) # set the value in the csv to this

            # clear the values for each of the widgets
            keys_list = list(self.codes_dict.keys())
            for key in range(len(keys_list)): 
                a_val = self.codes_dict[keys_list[key]]
                if len(a_val[1]) > 0:
                    this_string_var = self.b[key]
                    this_string_var.set("Select option")
                else:
                    this_string_var = self.b[key]
                    this_string_var.set("")
            
            # clear the label with the warning message
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

    def addCodes(self):
        for code in self.codes_dict.keys():
            print(code)
            if len(self.codes_dict[code]) > 1:
                print(self.codes_dict[code][1].get("1.0",END))
                va = self.codes_dict[code][1].get("1.0",END) # this extracts the text from the widget
                va = va.strip()
                va = va.strip(";")
                va = va.split(";")
                va = [el.strip() for el in va] # remove whitespaces from each option item itself
                #va = va.remove("\\n")
                print(va)
                self.codes_dict[code][1] = va   
            else:
                self.codes_dict[code].append([])
        
        # destroy the second old window
        self.win2.destroy()

        # now let's add these optionmenu to the main window
        keys = list(self.codes_dict.keys())
        self.updateMain(keys) # pass the list of keys into the next function: updateMenu

    def updateMain(self, keys):
        # destroy the old window
        self.win2.destroy()

        # create new window
        self.win_main = Toplevel()
        self.win_main.geometry("1250x700")
        self.win_main.minsize("700", "650") # width x height
        self.win_main.wm_title("Cody")

        # create a list of StringVars for only the continuous variables
        self.b = [StringVar(self.win_main) for i in range(len(keys))]

        for new_row in range(len(keys)): 
            self.main_labels = Label(self.win_main, text=keys[new_row])
            self.main_labels.grid(row= new_row+2, column=19, padx=(5, 15), pady=(0, 5), sticky=E)
            one_key = keys[new_row]
            one_val = self.codes_dict[one_key]
            print(one_val)

            if len(one_val[1]) > 0:
                SEL_OPTS = one_val[1]
                this_string_var = self.b[new_row]
                this_string_var.set("Select option")
                ddown = OptionMenu(self.win_main, self.b[new_row], *SEL_OPTS) 
                ddown.config(width=14)
                ddown.grid(row = new_row+2, column=20, sticky=W, padx=(5, 15), pady=(5, 10)) 
            else:
                self.main_entries = Entry(self.win_main, textvariable=self.b[new_row])
                self.main_entries.grid(row= new_row+2, column=20, padx = (5, 15), sticky=W, pady=(5, 10))
                #new_continuous_count += 1

        # this section sets which columns are the ones that move - weight is what will expand when expanded
        #self.pack(fill=BOTH, expand=True) # see if I can add this back later
        self.win_main.rowconfigure(5, pad=7)
        self.win_main.rowconfigure(17, weight=1)
        self.win_main.columnconfigure(3, weight=1)
        self.win_main.columnconfigure(3, pad=7)
        
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Import csv", command=self.import_csv_data)
        filemenu.add_separator()
        filemenu.add_command(label="Save", command=self.save)
        menubar.add_cascade(label="File", menu=filemenu)
        
        # FONT CONFIGURATIONS        
        font_label = Label(self.win_main, text="Font size")
        font_label.grid(row=1, column=19, pady=(10, 20), padx=(15,5), sticky=E)
        FONT_OPTS= ["11", "12", "13", "14", "16", "18", "20"]
        self.font_var = StringVar(self)
        self.font_var.set(FONT_OPTS[2]) # default value
        dropdown = OptionMenu(self.win_main, self.font_var, *FONT_OPTS, command=lambda _: self.getFont())
        dropdown.grid(row = 1, column=20, sticky=W, padx=(2, 15), pady=(10, 20)) 
        
        self.myFont = font.Font(family="Times New Roman", size=13)
        self.text_area = scrolledtext.ScrolledText(self.win_main, wrap = tkinter.WORD, width = 40, padx = 2, height = 10, font = self.myFont)
        # padx here is a internal buffer
        # FONT CONFIGURATIONS END
        
        #text_area.insert(INSERT, "")
        self.text_area.grid(row = 1, column = 0, columnspan=5, rowspan=25, pady = 10, padx = 15, sticky=N+S+E+W)
        
        next_btn = Button(self.win_main, text="Next row", command=self.next_row, width=11)
        next_btn.grid(row=len(keys)+3, column=20, padx = (2, 15), sticky=E, pady=(15, 10))
        
        self.labeltext_empty=StringVar()
        self.labeltext_empty.set("")
        self.empty_message = Label(self.win_main, justify=LEFT, textvariable=self.labeltext_empty)
        self.empty_message.config(fg="Red")
        self.empty_message.grid(row = len(keys)+4, column = 20, padx = (2, 15), pady = (15, 0),sticky=W)

        self.progress = Progressbar(self.win_main, orient = HORIZONTAL, length = 100, mode = 'determinate')
        self.progress.grid(row=26, column = 0, columnspan=5, pady = 3, padx = 15, sticky=N+S+E+W)

        if self.starting_row < len(self.df):
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
    
    root.title("Old Cody")
    root.geometry('1250x700') # width x height
    root.minsize("700", "650")
    app = Cody()
    root.mainloop()

if __name__ == '__main__':
    main()