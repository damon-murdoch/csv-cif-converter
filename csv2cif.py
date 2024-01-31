import csv
import sys

def convert_csv_to_cif(input_csv, output_cif):
    # Read the CSV file
    with open(input_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        lines = list(csv_reader)

    # Remove extraneous commas from header and trailer
    lines[0] = [item.replace(',', '') for item in lines[0]]
    lines[-1] = [item.replace(',', '') for item in lines[-1]]

    # Write the modified content to a CIF file
    with open(output_cif, 'w', newline='') as cif_file:
        csv_writer = csv.writer(cif_file)
        csv_writer.writerows(lines)

if __name__ == "__main__":

    # Get arguments
    args = sys.argv[1:]

    if len(args) > 0:

        input_csv_file = sys.argv[1]

        output_cif_file = input_csv_file.replace(".csv", ".cif")

        # Both input and output filename match
        if input_csv_file == output_cif_file: 
            raise TypeError(f"File {input_csv_file} does not have file type .csv!")

        if len(args) > 1: 
            output_cif_file = sys.argv[2]

        convert_csv_to_cif(input_csv_file, output_cif_file)

        print(f"Conversion completed. CIF file saved as {output_cif_file}")
    else:
        print("Usage: python script.py input_csv_file [output_cif_file]")
