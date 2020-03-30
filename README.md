# Easy_Quote
Downloads info from a spreadsheet on Google Sheets, then turns it into a CSV file where we can make queries on part numbers for items quoted in the past. Used to compare price and other changes on the items over time.

Programmed in Python 3

Coded and tested on:
  Linux Mint 18.2 Sonya
  Windows 10

----------------

The program uses hte "oauth2client" and "gspread" libraries to get the informaion on a spreadsheet on Google Sheets using the Google Drive API

----------------

The columns are:

1 = Date the quote was made / 2 = Part Number of product / 3 = Description of product / 4 = Quantity quoted / 5 = Cost of product to us / 6 = Price at which it was sold

--------------
