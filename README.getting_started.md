# Initial Setup
This section covers how to set up your Windows 10 dev environment

## Installation of Python
- Open a command prompt
- Type `python`
- If you get some text and `>>>` verify the text above says `Python 3.7.4` or later.  Type `exit()` to return to a command prompt.
- If nothing comes back, then another window to the Windows Store should open to the python page
- Install python from the Windows store
- Once installed type `python --version` to get the current version of Python, which should be `Python 3.7.4` or later

## Install Git for Windows
This is an optional step, will making updating the files a bit easier, but if you don't want to deal with it, you can always just download the .zip file from the main page

https://git-scm.com/downloads

## Cloning the repo
If managing zip files isn't your thing, this will be a bit easier with a few commands

- Pick a folder to be your working directory, for example `c:\Users\<loginid>\`
- Type `git clone https://github.com/joej164/CMN_File_Manipulation.git` to copy the files to your PC
- You should now have a folder named `CMN_File_Manipulation` in that directory

## Verify everything is working
Lets make sure you can run a basic program

- Make sure you are in the working directory `~\CMN_File_Manipulation.git`
- Type `python hello_world.py`  (Auto completion should work so `python he<tab>` should fill out the command
- You should have the text `You ran a python program` on the screen

# Updating files
As I update files, you'll want to pull down the latest versions.

- Navigate to the working directory `~\CMN_File_Manipulation.git`
- Type `git pull` and that should pull all the latest files and sync your local directory with the main repo

