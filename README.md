# CMN_File_Manipulation
A program for file manipulation for CMN csv files.

This was written assuming the use of Windows 10 with current updates as of 15-Sept-2019

This was also written to use as much of the Python standard library as possible to minimze the need to install packages.

These were also written in such a was as for a non-software developer to be able to understand them troubleshoot them if necessary.

# Getting Started
Read the following document for information on how to install Python and set up your machine
[README.getting_started.md](README.getting_started.md)

# Running the program 

## Update the variables at the top
At the top of the program are a number of constants you can set if the file format changes.
All of these fields are case sensitive.

* `CONTRIBUTION_COLUMN_HEADER` - This is the name of the header that all the raffle tickets are calculated from
* `UNIQUE_ID_COLUMN_HEADER` - Identifies which column in the file is used to uniquely identify a person
* `DATE_OF_DONATION_COLUMN_HEADER` - Used to identify the date column
* `NUMBER_OF_WINNERS` - Update this based on the number of tickets that need to be selected
* `DONATION_TICKET_CONVERSION` - This identifies the table used for calculating the number of tickets based on the donation size

## Run the program
```python raffle_program.py```   (Windows)
```python3 raffle_program.py```  (Mac or Linux)

- Put all your source CSV files in the `input_files` folder
- All files must have the same number of columns and the same column headers (files must all be the same format)
- Output of the data files into a file in the `output_files` folder

