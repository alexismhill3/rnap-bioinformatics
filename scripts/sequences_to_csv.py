import csv
import sys

def read_fasta(fasta_path):
    sequences = {}
    current_sequence = None

    with open(fasta_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                # Header line, indicating a new sequence
                sequence_name = line[1:]
                sequences[sequence_name] = ''
                current_sequence = sequence_name
            else:
                # Sequence line, append to the current sequence
                sequences[current_sequence] += line

    return sequences

if __name__ == "__main__":
    fasta_path = sys.argv[1]
    output_file = sys.argv[2]
    sequences = read_fasta(fasta_path)

    with open(output_file, 'w', newline='') as f_output:
        csv_writer = csv.writer(f_output)
        csv_writer.writerow(["Protein_ID", "Sequence"]) # Header
        for sequence_name, sequence in sequences.items():
            csv_writer.writerow([sequence_name, sequence])
        
