from Bio import SeqIO
import sys

def get_total_length(file_path):
    total_length = 0
    with open(file_path, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            total_length += len(record.seq)
    return total_length

def convert_to_m8e(m8_file_path, fasta_file_path, output_file_path):
    # Calculate the total length of the fasta file
    fasta_length = get_total_length(fasta_file_path)

    # Read the m8 file contents
    with open(m8_file_path, "r") as m8_file:
        m8_lines = m8_file.readlines()

    # Write to the m8e file
    with open(output_file_path, "w") as output_file:
        # Write the fasta length as the first row
        output_file.write(f"Length:{fasta_length}\n")
        # Append the rest of the m8 content
        output_file.writelines(m8_lines)

    print(f"Converted {m8_file_path} and {fasta_file_path} to {output_file_path} in m8e format.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script_name.py <input.m8> <input.fasta> <output.m8e>")
        sys.exit(1)

    m8_file_path = sys.argv[1]
    fasta_file_path = sys.argv[2]
    output_file_path = sys.argv[3]

    convert_to_m8e(m8_file_path, fasta_file_path, output_file_path)
