# Program to combine multiple CSV files into a single CSV file
import pathlib
import csv
import time


def list_files_to_combine():
    # List of CSV files to return
    files = []

    # Search the input_files directory
    currentDirectory = pathlib.Path('./input_files')

    # Set the type of files we want to read
    file_pattern = "*.csv"

    # Read in all the CSV files from the input directory
    for file in currentDirectory.glob(file_pattern):
        files.append(file)
        print(f'Adding the following file to the list of files: {file}')

    # Verify there are CSV files in the directory
    if not files:
        raise ValueError("There must be at least one CSV file in the `input_files` folder")

    return files


def read_in_csv_files(files):
    # This function reads in the data from the files
    # and combines them into a list of dictionaries

    output = []
    for file in files:
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                output.append(dict(row))

    # Verify there data in the files
    if not files:
        raise ValueError("The CSV files were blank, there must be at least one entry")

    return output


def write_out_csv_file(data):
    # Figure out the header names from the first entry
    field_names = list(data[0].keys())
    timestr = time.strftime("%Y%m%d-%H%M%S")
    output_file_name = f'output_files\combined_output_{timestr}.csv'

    # Write all the data out to a new CSV file
    with open(output_file_name, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()

        for row in data:
            writer.writerow(row)

    print(f"All data output to filename: {output_file_name}")


def main():
    print("Starting the CSV Merge Script")
    csv_files = list_files_to_combine()

    print("Read the CSV files into memory")
    csv_data = read_in_csv_files(csv_files)

    print("Write the data out to a file")
    write_out_csv_file(csv_data)


if __name__ == "__main__":
    main()
