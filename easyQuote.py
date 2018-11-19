from tkinter import *
import csv
import sys
import xlsxwriter
import os

############################# Find Part Number function
def readFile(partNumberWanted):
        
    x = 0
    rowWithPartNumber = []

    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]          # Search over different months 2016
    for currentMonth in months:

        with open("2016inventory/" + currentMonth + ".csv", "r") as invenFile:        #open each csv file
            invenFileReader = csv.reader(invenFile)
            for row in invenFileReader:
                if row[1].upper() == partNumberWanted:            # Check Part Number
                    rowWithPartNumber.append(row[0:5])     # Take values from date to final price
                    x += 1


        invenFile.close()

    return (rowWithPartNumber, x)


###################### Create file with selecter rows
def appendFile(rowWithPartNumber):


    with open("sampleRows.csv", "w") as sampleFile:
        sampleFileWriter = csv.writer(sampleFile)

        for row in rowWithPartNumber:
            sampleFileWriter.writerow(row)     #Write row w/ Part Num. at the end

    sampleFile.close()

    return(sampleFileWriter)



#################### Turn selected rows on CSV to XlSX
def turnCsvToXlsx(sampleFileWriter):

    r = 0

    wb = xlsxwriter.Workbook("sampleRows.xlsx")
    ws = wb.add_worksheet("Sample")

    

    for row in sampleFileWriter:
        ws.write_row(r, 0, row)
        r += 1
    wb.close()

    os.system('libreoffice sampleRows.xlsx')        # Open file with LibreOffice



############ Main class
class mainClass(Frame):

    def   __init__(self, master):

        super().__init__(master)  

        self.master  

        self.label1 = Label(master, text = "Write Part Number:")
        self.entry = Entry(master)                  # Part Number searched goes here
        self.entry.bind("<Return>", lambda _: self.searching(self.entry.get()))        #Use button "Search" when Enter is pressed
        self.entry.bind("<F1>", self.erasing)            # Clear text with F1
        self.entry.focus_set()          #Start cursor here
        self.search_button = Button(master, text="Search", command = lambda: self.searching(self.entry.get()))              # Search button

        #Layout
        self.label1.grid(row = 0, column = 0, sticky = W)
        self.entry.grid(row = 1, column = 0, columnspan = 3, )
        self.search_button.grid(row = 2, column = 0)

        self.bind_all("<Escape>", self.quit)              #Close window with ESC key




############## Search for Part Number
    def searching(self, partNumberWanted):
    
        rowWithPartNumber, y = readFile(partNumberWanted)     #readFile function

        if y > 0:
            sampleFileWriter = appendFile(rowWithPartNumber)        # Create CSV file with rows with part number
            turnCsvToXlsx(rowWithPartNumber)                        # Create Excel file with rows with part number


############ Erase everything
    def erasing(self, event):
        self.entry.delete(0,END)                        #clear entry element


########### Close window
    def quit(self, event):
        Frame.quit(self)
        



root = Tk()                  #create window
#root.resizable(1, 1)         #change for different screen sizes
root.title("Line copier")       # title of window
app = mainClass(master = root)
app.mainloop()

