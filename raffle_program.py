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
            line = 'initial_value'
            while CONTRIBUTION_COLUMN_HEADER not in line and line:
                print(line)
                line = csvfile.readline()

            # Define the file_header_list
            print(line)
            file_headers_list = line.rstrip().split(',')
            print(file_headers_list)
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
    output_file_name = pathlib.Path('output_files', f'{file_prefix}_{timestr}.csv')

    # Write all the data out to a new CSV file
    with open(output_file_name, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()

        for row in data:
            writer.writerow(row)

    print(f"All data output to filename: {output_file_name}")


def merge_donations(csv_data, identifier_header, contribution_header, date_header):
    # This function finds all duplicate entries and merges them into a single entry

    if not isinstance(csv_data, list):
        raise TypeError("`csv_data` must be a list")

    params = [identifier_header, contribution_header, date_header]
    if not all([isinstance(x, str) for x in params]):
        raise TypeError("All headers must be strings")

    data = {}
    for row in csv_data:
        # Verify the contribution is a valid format
        try:
            contribution = int(float(row[contribution_header]))

            if row[identifier_header] in data.keys():
                print(f'Found a duplicate entry for: {row[identifier_header]}')
                id = row[identifier_header]
                data[id][contribution_header] += contribution
                data[id][date_header] += f"\r\n{row[date_header]}"
                data[id]['file_name'] += f"\r\n{row['file_name']}"
            else:
                key = row[identifier_header]
                data[key] = {}
                for k, v in row.items():
                    data[key][k] = str(v)
                data[key][contribution_header] = contribution
        except ValueError:
            print(f"Skipping user contribution found with invalid donation: {row}")

    output = []

    # Convert the data back to a list of dicts
    for k, v in data.items():
        output.append(v)

    return output


def calculate_raffle_entries(csv_data, donation_dict):
    if not isinstance(csv_data, list):
        raise TypeError("`csv_data` must be a list")

    if not isinstance(donation_dict, dict):
        raise TypeError("`donation_dict` must be a dictionary")

    ticket_lookup_dict = create_ticket_lookup_dict(donation_dict)

    for row in csv_data:
        donation = row[CONTRIBUTION_COLUMN_HEADER]
        if donation >= 200:
            row['tickets'] = 100
        else:
            row['tickets'] = ticket_lookup_dict[donation]

    return csv_data


def create_ticket_lookup_dict(donation_def):
    # Verify that a dictionary was passed to the function
    if not isinstance(donation_def, dict):
        raise TypeError("Must pass a dictionary to this function")

    # Verify that all the keys in the dict are integers
    if not all([True if isinstance(x, int) else False for x in donation_def.keys()]):
        raise TypeError("All the keys in the donation dict must be integers")

    # Verify that all the values dict are integers
    if not all([True if isinstance(x, int) else False for x in donation_def.values()]):
        raise TypeError("All the values in the donation dict must be integers")

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


# Creates a list of all the users with valid email addresses
# Also adds a `tickets` column to all rows
def create_raffle_list(csv_data):
    # Verify that a list was passed to the function
    if not isinstance(csv_data, list):
        raise TypeError("Must pass a list to this function")

    # Verify that all items in the list are dictionaries
    if not all([True if isinstance(x, dict) else False for x in csv_data]):
        raise ValueError("All items in the data structure must be dictionaries")

    raffle_list = []
    for row in csv_data:
        id = row[UNIQUE_ID_COLUMN_HEADER]
        valid_email = True if "@" in id and "." in id else False

        if valid_email is True and row['tickets'] > 0:
            for x in range(row['tickets']):
                row_cpy = copy.deepcopy(row)
                row_cpy['is_winner'] = False

                raffle_list.append(row_cpy)

    return raffle_list


def pick_raffle_winners(raffle_list, qty_winners):
    if not isinstance(raffle_list, list):
        raise TypeError("`raffle_list` must be a list")

    if not isinstance(qty_winners, int):
        raise TypeError("`qty_winners` must be an integer")

    total_tickets = len(raffle_list)

    try:
        winners = random.sample(range(0, total_tickets), qty_winners)
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
    csv_data = merge_donations(csv_data,
                               UNIQUE_ID_COLUMN_HEADER,
                               CONTRIBUTION_COLUMN_HEADER,
                               DATE_OF_DONATION_COLUMN_HEADER)

    print("Write out the data with combined money")
    write_out_csv_file(csv_data, "combined_donation_output")

    print("Calculate number of Raffle Entries per person")
    csv_data = calculate_raffle_entries(csv_data, DONATION_TICKET_CONVERSION)

    print("Write out the data with total raffle tickets")
    write_out_csv_file(csv_data, "raffle_tickets_per_user")

    print("Create a list of entries for each user with valid email address and not anonymous")
    raffle_list = create_raffle_list(csv_data)

    print("Write out the data with total raffle tickets")
    write_out_csv_file(raffle_list, "expanded_raffle_entries")

    print("Pick winners from the raffle list")
    winner_list = pick_raffle_winners(raffle_list, NUMBER_OF_WINNERS)

    print("Write out the winners and non-winners")
    write_out_csv_file(winner_list, "winner_list_entries")


if __name__ == "__main__":
    main()
