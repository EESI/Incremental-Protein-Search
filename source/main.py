import sys
from merger import merge_m8_files

def main():
    # example: python main.py blastp_astral_scope_result2.m8 blastp_astral_scope_result3.m8 merge_blastp_astral_scope_result23.m8 6205115 6211928
    if len(sys.argv) != 6:
        print("Usage: python main.py <file1> <file2> <output_file> <part_db_len1> <part_db_len2>")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    output_file = sys.argv[3]
    part_db_len1 = int(sys.argv[4])
    part_db_len2 = int(sys.argv[5])
    
    print("====================================")
    print("Starting Incremental Protein Search m8 file merger")
    print("------------------------------------")
    print(f"Input file 1: {file1}")
    print(f"Input file 2: {file2}")
    print(f"Output file: {output_file}")
    print(f"Database length for file 1: {part_db_len1}")
    print(f"Database length for file 2: {part_db_len2}")
    print("====================================\n")

    merge_m8_files(file1, file2, output_file, part_db_len1, part_db_len2)

if __name__ == "__main__":
    main()