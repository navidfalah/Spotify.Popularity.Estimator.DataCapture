import csv

def remove_first_column(input_csv, output_csv):
    with open(input_csv, 'r', newline='') as infile:
        with open(output_csv, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            for row in reader:
                # Remove the first element (column) from each row
                del row[0]
                writer.writerow(row)

# Example usage:
input_csv = 'all_spotify_data.csv'
output_csv = 'all_spotify_data_refined.csv'
remove_first_column(input_csv, output_csv)
