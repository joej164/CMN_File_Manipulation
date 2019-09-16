# Program to combine multiple CSV files into a single CSV file

# All csv inputs should be of the same format or weird issues will occur
import pathlib
import csv
import time
import random
import copy

# Name of a column that has the donation
CONTRIBUTION_COLUMN_HEADER = "Amount"

# Name of the column header that is a unique ID for all donators
# Typically the email address
UNIQUE_ID_COLUMN_HEADER = "Email"

# Name of the column header that has the date of donations
DATE_OF_DONATION_COLUMN_HEADER = "Date/Time (ET)"

# Number of winners to pick
NUMBER_OF_WINNERS = 10

DONATION_TICKET_CONVERSION = {
        10: 1,
        25: 5,
        50: 10,
        75: 18,
        100: 30,
        125: 45,
        150: 65,
        200: 100
        }


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
        with open(file, newline='', encoding='utf8') as csvfile:
            # Remove leading lines from the CSV file
            line = ''
            while CONTRIBUTION_COLUMN_HEADER not in line:
                line = csvfile.readline()

            # Define the file_header_list
            file_headers_list = line.rstrip().split(',')

            # Read in the data into memory
            reader = csv.DictReader(csvfile, fieldnames=file_headers_list)
            for row in reader:
                # Append the file name to the entry to know where it came from
                row["file_name"] = file

                output.append(dict(row))

    # Verify there data in the files
    if not output:
        raise ValueError("The CSV files were blank, there must be at least one entry")

    return output


def write_out_csv_file(data, file_prefix=None):
    if not file_prefix:
        file_prefix = "default_output"

    # Figure out the header names from the first entry
    field_names = list(data[0].keys())
    timestr = time.strftime("%Y%m%d-%H%M%S")
    output_file_name = f'output_files\\{file_prefix}_{timestr}.csv'

    # Write all the data out to a new CSV file
    with open(output_file_name, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()

        for row in data:
            writer.writerow(row)

    print(f"All data output to filename: {output_file_name}")


def merge_donations(csv_data):
    # This function finds all duplicate entries and merges them into a single entry
    data = {}
    for row in csv_data:
        if row[UNIQUE_ID_COLUMN_HEADER] in data.keys():
            print(f'Found a duplicate entry for: {row[UNIQUE_ID_COLUMN_HEADER]}')
            id = row[UNIQUE_ID_COLUMN_HEADER]
            data[id][CONTRIBUTION_COLUMN_HEADER] += int(float(row[CONTRIBUTION_COLUMN_HEADER]))
            data[id][DATE_OF_DONATION_COLUMN_HEADER] += f"\r\n{row[DATE_OF_DONATION_COLUMN_HEADER]}"
            data[id]['file_name'] += f"\r\n{row['file_name']}"
        else:
            key = row[UNIQUE_ID_COLUMN_HEADER]
            data[key] = {}
            for k, v in row.items():
                data[key][k] = str(v)

            # Convert the donation amount to an integer
            try:
                data[key][CONTRIBUTION_COLUMN_HEADER] = int(float(data[key][CONTRIBUTION_COLUMN_HEADER]))
            except ValueError:
                print(f"User found with invalid donation: {row}")

    output = []

    # Convert the data back to a list of dicts
    for k, v in data.items():
        output.append(v)

    return output


def calculate_raffle_entries(csv_data):
    ticket_lookup_dict = create_ticket_lookup_dict(DONATION_TICKET_CONVERSION)
    for row in csv_data:
        donation = row[CONTRIBUTION_COLUMN_HEADER]
        if donation >= 200:
            row['tickets'] = 100
        else:
            row['tickets'] = ticket_lookup_dict[donation]

    return csv_data


def create_ticket_lookup_dict(donation_def):
    d = {}
    current = 0
    previous = 0
    tickets = 0
    for k, v in donation_def.items():
        current = k
        for x in range(previous, current):
            d[x] = tickets
        previous = current
        tickets = v

    return d


def create_raffle_list(csv_data):
    rl = []
    for row in csv_data:
        id = row[UNIQUE_ID_COLUMN_HEADER]
        valid_email = True if "@" in id and "." in id else False

        if valid_email is True and row['tickets'] > 0:
            for x in range(row['tickets']):
                row_cpy = copy.deepcopy(row)
                row_cpy['is_winner'] = False

                rl.append(row_cpy)

    return rl


def pick_raffle_winners(raffle_list):
    total_tickets = len(raffle_list)

    try:
        winners = random.sample(range(1, total_tickets + 1), NUMBER_OF_WINNERS)
    except ValueError:
        raise ValueError("You selected more winners than tickets")

    for w in winners:
        raffle_list[w]['is_winner'] = True

    return raffle_list


def main():
    print("Starting the CSV Merge Script")
    csv_files = list_files_to_combine()

    print("Read the CSV files into memory")
    csv_data = read_in_csv_files(csv_files)

    print("Write the data out to a file")
    write_out_csv_file(csv_data, "all_files_merged_output")

    print("Find all duplicate email addresses, and combine the donations")
    csv_data = merge_donations(csv_data)

    print("Write out the data with combined money")
    write_out_csv_file(csv_data, "combined_donation_output")

    print("Calculate number of Raffle Entries per person")
    csv_data = calculate_raffle_entries(csv_data)

    print("Write out the data with total raffle tickets")
    write_out_csv_file(csv_data, "raffle_tickets_per_user")

    print("Create a list of entries for each user with valid email address and not anonymous")
    raffle_list = create_raffle_list(csv_data)

    print("Write out the data with total raffle tickets")
    write_out_csv_file(raffle_list, "expanded_raffle_entries")

    print("Pick winners from the raffle list")
    winner_list = pick_raffle_winners(raffle_list)

    print("Write out the winners and non-winners")
    write_out_csv_file(winner_list, "winner_list_entries")


if __name__ == "__main__":
    main()
