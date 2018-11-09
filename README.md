# nhs-scanner
ID Scanner for Bellaire NHS

# Usage
- To run the ID scanner, simply click on the Run_Scanner_MAC or Run_Scanner_WINDOWS.py file (depending on the operating system).
- ID numbers can either be scanned with a barcode scanner or manually entered.
- To end the program, just click the X in the corner

# Important Information
- The program creates a CSV file in the same folder as Run_Scanner that contains the date, name, and ID number of all students scanned in a given session. This file can be viewed with Excel.

# Requirements
- Python 2.7 must be installed on the computer running this script. If it is not installed, you can install it here: https://www.python.org/downloads/release/python-2715/

## Updating The Student List
The list of all student information is saved in the data folder. To update this list, the new file will need the same name and columns as the original file.
Steps to create a new CSV file:
- Open the file in Excel, and ensure that the columns are: (Last Name, First Name, Grade, ID #)
- Save the file as Student_List.csv
-- Open the file in Excel
-- Click File > Save As
-- Enter Student_List as the file name
-- Choose Windows Comma Separated (CSV) as the file type
-- Choose the data/ folder as the location to save the new file (or move the csv file there after you create it)
- NOTE: DO NOT SHARE the student data file or commit it to the repository.

## Creating new .zip file on mac
- Navigate to project folder in terminal
- Run the following: 
zip -r nhs-scanner.zip . -x ".*" -x "*.pyc"

**For further inquiry, ask the Bellaire CS Club.**