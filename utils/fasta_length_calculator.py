from Bio import SeqIO
import sys

def get_total_length(file_path):
    total_length = 0
    with open(file_path, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            total_length += len(record.seq)
    return total_length

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <fasta_file_path>")
        sys.exit(1)
    
    fasta_file = sys.argv[1]
    total_length = get_total_length(fasta_file)
    print(f"Total sequence length: {total_length}")
