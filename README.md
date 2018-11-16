# easyQuote-Python
Used to check past quotes, compare them and add new ones

Python 3

Coded and tested on Linux Mint 18.2 Sonya

Originally, the quotes file was an .xlsx file with a sheet for each month. Each of the sheets was exported as a .csv file and put under the folder called "2016inventory".

This code is a simple GUI in where you enter an item's Part Number when you want to check if it has been quoted before. It goes month by month and at the end it opens LibreOffice with a .xlsx file with the rows that have the information of each of the times that Part Number was quoted.

It simplifies the task of comparing the change in prices. Also you can copy the row of the last time the item was quoted and copy it into the .xlsx file you are currently working on.

----------------

There columns are:

1 = Date the quote was made - 2 = Part Number of product - 3 = Price bought - 4 = Percent added to bought price - 5 = Price at which it was sold - 6 = Profit made

--------------
