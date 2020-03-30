# Easy_Quote
Downloads info from a spreadsheet on Google Sheets, then turns it into a CSV file where we can make queries on part numbers for items quoted in the past. Used to compare price and other changes on the items over time.

Programmed in Python 3
2019-2020

Coded and tested on:
  Linux Mint 18.2 Sonya
  Windows 10

----------------

The program uses the "oauth2client" and "gspread" libraries to get the informaion on a spreadsheet on Google Sheets using the Google Drive API. The information from the spreadsheet is written into a CSV file using the "CSV" library. The file is called "quotesFile.csv".

After that, a GUI is created using the "Tkinker" library. The GUI only consists of an Entry field and a Button. On the field we write the part number we are looking for and then click Enter or click the button.

Using the "CSV" library we read from the "quotesFile.csv" searching for the part number. If there is no item with that part number then the string "Times quoted: 0" is returned. If there is indeed an item with that part number then a new CSV file named "sampleRows.csv" where it writes all the times the item was quoted.

----------------

The columns are:

1 = Date the quote was made / 2 = Part Number of product / 3 = Description of product / 4 = Quantity quoted / 5 = Cost of product to us / 6 = Price at which it was sold

--------------
