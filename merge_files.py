# Program to combine multiple CSV files into a single CSV file
import pathlib 

def list_files_to_combine():
    # List of CSV files to return
    csv_files = []

    # Search the input_files directory
    currentDirectory = pathlib.Path('./input_files')

    # Set the type of files we want to read
    file_pattern = "*.csv"

    # Read in all the CSV files from the input directory
    for file in currentDirectory.glob(file_pattern):
        csv_files.append(file) 

    # Verify there are CSV files in the directory
    if not csv_files:
        raise ValueError("There must be at least one CSV file in the `input_files` folder")

    print(csv_files)

def main():
    print("Starting the CSV Merge Script")
    list_files_to_combine()


if __name__ == "__main__":
    main()
