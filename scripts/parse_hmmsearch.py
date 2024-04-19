import csv
import sys

def parse_space_delimited_hmmsearch_output(input_file, output_file):
    # read in hmmsearch output
    with open(input_file, 'r') as f_input:
        lines = f_input.readlines()

        # parse lines and write to csv
        with open(output_file, 'w', newline='') as f_output:
            csv_writer = csv.writer(f_output)
            for index, line in enumerate(lines):
                data = line.strip().split()
                if index == 1: # parse column names from line 1
                    data.pop(0) 
                    data = [x for x in data if x != "name"]
                    data.pop(-1)
                    data.pop(-1)
                    for i in range(7, 10):
                        data[i] = data[i] + "-best-domain"
                elif data[0][0] == "#": # skip headers/footers
                    continue
                csv_writer.writerow(data)


if __name__ == "__main__":
    input_file = sys.argv[1]  
    output_file = sys.argv[2] 

    parse_space_delimited_hmmsearch_output(input_file, output_file)
