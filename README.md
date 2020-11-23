# easyQuote
Reads a series of CSV files that have quotes made on products accross time. In this case there are only 3 files as an example. In a simple GUI you write the part number of the product you are looking for, and the script will iterate through the CSV files and return a new CSV file with the times the product was quoted, making it easier to compare changes in prices over time.

Programmed in Python
2020

Written and tested on:
  Linux Mint 18.2 Sonya
  Windows 10

----------------

The script displays a simple GUI with a text input and a button. You should write the part number of the product you are looking for in the text input, then click on the button. The program will go to a folder called "inv/" and iterate over the CSV files on that are inside the folder (in this case there are only 3 files "jan", "feb", and "mar" with a couple of quotes on each, as an exmple).

On each CSV file, the script will find all the times the selected part number was quoted, and return on a new CSV file called "sampleRows.csv" all the times the part number was quoted, making it easier to compare changes in prices over time. The script and the CSV files can be modified to display other variables like stock, or whatever the user needs about the products.

----------------

The columns are:

1 = Date the quote was made / 2 = Part Number of product / 3 = Description of product / 5 = Price of product

--------------
