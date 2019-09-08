# CMN_File_Manipulation
A collection of scripts for file manipulation for CMN csv files.

This was written assuming the use of Windows 10 with current updates as of 8-Sept-2019

This was also written to use as much of the standard library as possible to minimze the need to install packages.

These were also written in such a was as for a non-software developer to be able to understand them troubleshoot them if necessary.

# Getting Started
Read the following document for information on how to install Python and set up your machine
[README.getting_started.md](README.getting_started.md)

# Running specific scripts
This section includes links to each part of the script

## Merging multiple csv files into a single csv file
```python merge_files.py```

- Put all your source files in the `input_files` folder
- All files must have the same number of columns and the same column headers
- Output the data into a file in the `output_files` folder

### Issues or Concerns
Currently this is bad data in, bad data out.  No data validation is done if any data is missing.  This can be done in a future script or a modification of this script if it seems like a good idea.

# This is what I think needs done, please review
Please review, based on what I've heard you need, 

- Merge multiple `csv` files into a single master file
- Combine users who contributed multiple times into a single entry with a total amount of money contributed
- Determine the number of tickets each user gets
- Randomly select X number of tickets from the pool of total tickets
- Create a csv with winners and addresses to mail the prizes to

Each of the items I see as a seperate script.  I could write a large program, but initialy i'm thinking a bunch of small scripts would be easier for you to use and comprehend.  I could be wrong also..




