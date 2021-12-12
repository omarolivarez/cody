# cody
A desktop app for coding (labeling) data. Cody is made from a Python backend, tkinter front-end, and pandas for data management.  
*Screenshot of Cody*
![Cody screenshot](https://github.com/omarolivarez/cody/blob/dev/CODY/images/Cody_example.png)


## Problem it solves
Coding (labeling) data that consists of long-text entries can be tough. If you import it into Excel, you have to do a combination of shrinking the font, expanding the cell size, and toggling across cells to make your entries. When text entries get to be pretty long, using Excel as your coding environment can be cumbersome and time consuming. 

## How Cody solves it
Cody serves as a desktop UI specifically designed for people who need to code long text datasets. 

## How to get Cody running
For right now, Cody is not downloadable as an executable. But in the meantime, you can "git clone cody" to your computer and run using "python cody.py" from the top-most "cody" folder. 

## How to use Cody
1. Make sure the column containing the text is the first column in the CSV. Cody can only code one text column. Cody allows for up to 15 codes to use on your data. Past 15 codes and the UI becomes crowded and hard to use.
2. Click "File > Imort CSV" in the menu options. 
3. Select the CSV you're working with
4. Adjust the settings for each code. You have the option to identify each code as continuous or categorical. If categorical, you will be prompted to add the categories for the code, separated by a semicolon. When coding you will be able to select from these options from a dropdown. If you select continuous you will not receive the entry prompt and instead will have to type in your values during coding. Decimals and integers will be allowed but not text. 
5. The first row with missing entries will appear
6. Code away!

## Feedback welcome
Please feel free to share your ideas, bugs found, and features enhancements.
