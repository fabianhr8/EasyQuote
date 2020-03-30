import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv
from tkinter import *
import os

class easyQuote:

    def __init__(self, master):
        self.master = master
        master.title("Easy Quote")

        self.googleDocToCsv()               # Get all info on Google Docs spreadsheet into CSV file

        self.writeNum_label = Label(master, text = "Write Part Number:")
        self.writeNum_label.grid(row = 0, column = 0, sticky = W)
        self.writeNum_entry = Entry(master)                  # Part Number searched goes here
        self.writeNum_entry.grid(row = 1, column = 0, columnspan = 3)
        self.writeNum_entry.bind("<Return>", lambda _: self.searching(self.writeNum_entry.get()))        #Use button "Search" when Enter is pressed (TN310BK)
        self.writeNum_entry.bind("<F1>", self.erasing)            # Clear text with F1
        self.writeNum_entry.focus_set()          #Start cursor here
        self.search_btn = Button(master, text="Search", command = lambda: self.searching(self.writeNum_entry.get()))              # Search button
        self.search_btn.grid(row = 2, column = 0)

    
        self.frame = Frame(root)
        self.frame.bind_all("<Escape>", self.quit)
        

    ###################### Get spreadsheet from Google Drive and make CVS file
    def googleDocToCsv(self):
        scope = ['https://www.googleapis.com/auth/drive']          # Scope for Google API for Google Drive
        creds = ServiceAccountCredentials.from_json_keyfile_name('quote_secret.json', scope)
        client = gspread.authorize(creds)

        sheet = client.open('q_test').sheet1         # 'q_test' is the name of the spreadsheet
        
        quotes = sheet.get_all_records()
        print(type(quotes))

        with open("quotesFile.csv", "w", newline='', encoding='utf-8') as quotesFile:

            myFields = ["Date", "P/N",	"Description", "Qty", "CostForUs", "GivenPrice"]
            writer = csv.DictWriter(quotesFile, fieldnames=myFields)
            writer.writeheader()                                               # Write headers in row 1 (myFields)

            for row in quotes:                                                 # Write each row
                writer.writerow(row)


    ################## First function to search part numbers
    def searching(self, partNumberWanted):
        rowWithPartNumber, line_counter = self.readFile(partNumberWanted)     #readFile function

        if line_counter > 0:
            sampleFileWriter = self.appendFile(rowWithPartNumber)        # Create CSV file with rows with part number
            #turnCsvToXlsx(rowWithPartNumber)                        # Create Excel file with rows with part number


    ################# Read CSV files
    def readFile(self,partNumberWanted):

        line_counter = 0
        rowWithPartNumber = []

        with open("quotesFile.csv", "r", encoding="utf-8") as invenFile:        #open each csv file
            invenFileReader = csv.reader(invenFile)
            for row in invenFileReader:

                if row[1].upper() == partNumberWanted.upper():            # Check Part Number
                    rowWithPartNumber.append(row)     # Take values from date to final price
                    line_counter += 1
                else:
                    continue

            invenFile.close()

        print("Times quoted " + str(line_counter))
        return (rowWithPartNumber, line_counter)


    ############ Create CSV file w/ times quoted
    def appendFile(self, rowWithPartNumber):

        with open("sampleRows.csv", "w", newline='') as sampleFile:
            sampleFileWriter = csv.writer(sampleFile)

            for row in rowWithPartNumber:
                sampleFileWriter.writerow(row)     #Write row w/ Part Num. at the end

        sampleFile.close()
        os.system("sampleRows.csv")             # Open file in Excel
        return(sampleFileWriter)

        invenFile.close()

        print("Times quoted " + str(line_counter))
        return (rowWithPartNumber, line_counter)


    ########### Use F1 to erase text on search bar
    def erasing(self, event):
        self.writeNum_entry.delete(0,END)                        #clear entry element


    ########## Quit program
    def quit(self, event):
        root.destroy()
 

root = Tk()  
easy_q = easyQuote(root)
root.mainloop()
