import csv
import sys


def read_csv(csv_path):
    sequences = []
    try:
        with open(csv_path, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)  # Read the header row
            for row in csv_reader:
                sequences.append(row)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return sequences


if __name__ == "__main__":
    csv_path = sys.argv[1]
    output_path = sys.argv[2]
    sequences = read_csv(csv_path)

    with open(output_path, mode='w', newline='') as file:
        for entry in sequences:
            file.write(f">{entry[0]}\n")
            file.write(f"{entry[1]}\n")
    