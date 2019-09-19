# Initial Setup on Windows
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

- Make sure you are in the working directory `~\CMN_File_Manipulation`
- Type `python hello_world.py`  (Auto completion should work so `python he<tab>` should fill out the command
- You should have the text `You ran a python program` on the screen

# Updating files
As I update files, you'll want to pull down the latest versions.

- Navigate to the working directory `~\CMN_File_Manipulation`
- Type `git pull` and that should pull all the latest files and sync your local directory with the main repo

NOTE: If you've updated the settings in the program, for example, more than 10 winners, you'll need to reset
the files before doing a git pull by doing a `git reset --hard` and that will delete all changes to tracked files


# Initial Setup on Mac
This section covers how to set up your Mac to work with the program

NOTE: Python2 comes pre-installed on your Mac as part of the OS.  This version of Python is not compatible with this program.

## Installation of Python
- Navigate to `https://www.python.org/`
- Select `Downloads` and then click `Mac OS X`
- Click to download `Latest Python 3 Realease - Python 3.x.x`
- At the bottom click to download the `macOS 64-bit installer`
- Open the pkg file and follow the prompts to install Python on your Mac
- A windows should open up to the `Python 3.7` folder
- Double click on the `Install Certificates.command` file to install some required ssl certs

## Cloning the repo
If managing zip files isn't your thing, this will be a bit easier with a few commands

- Pick a folder to be your working directory, for example `/Users/<loginid>/`
- Type `git clone https://github.com/joej164/CMN_File_Manipulation.git` to copy the files to your PC
- You should now have a folder named `CMN_File_Manipulation` in that directory

## Verify everything is working
Lets make sure you can run a basic program

- Make sure you are in the working directory `~/CMN_File_Manipulation.git`
- Type `python3 hello_world.py`  (Auto completion should work so `python3 he<tab>` should fill out the command
- You should have the text `You ran a python program` on the screen

# Updating files
As I update files, you'll want to pull down the latest versions.

- Navigate to the working directory `~/CMN_File_Manipulation`
- Type `git pull` and that should pull all the latest files and sync your local directory with the main repo

NOTE: If you've updated the settings in the program, for example, more than 10 winners, you'll need to reset
the files before doing a git pull by doing a `git reset --hard` and that will delete all changes to tracked files
