import sys
from merger import merge_m8_files, merge_m8e_files



# example: python main.py --default blastp_astral_scope_result2.m8 blastp_astral_scope_result3.m8 merge_blastp_astral_scope_result23.m8 6205115 6211928

# example2: python main.py --extension blastp_astral_scope_result2.m8e blastp_astral_scope_result3.m8e merge_blastp_astral_scope_result23.m8e

    
def main():
    if len(sys.argv) < 5:
        print("Usage:")
        print("  python main.py --default <file1> <file2> <output_file> <part_db_len1> <part_db_len2>")
        print("  python main.py --extension <file1> <file2> <output_file>")
        sys.exit(1)

    mode = sys.argv[1]
    
    if mode == '--default':
        if len(sys.argv) != 7:
            print("Usage: python main.py --default <file1> <file2> <output_file> <part_db_len1> <part_db_len2>")
            sys.exit(1)
        
        file1 = sys.argv[2]
        file2 = sys.argv[3]
        output_file = sys.argv[4]
        part_db_len1 = int(sys.argv[5])
        part_db_len2 = int(sys.argv[6])
        
        print("====================================")
        print("Starting Incremental Protein Search m8 file merger (default mode)")
        print("------------------------------------")
        print(f"Input file 1: {file1}")
        print(f"Input file 2: {file2}")
        print(f"Output file: {output_file}")
        print(f"Database length for file 1: {part_db_len1}")
        print(f"Database length for file 2: {part_db_len2}")
        print("====================================\n")
        
        merge_m8_files(file1, file2, output_file, part_db_len1, part_db_len2)
    
    elif mode == '--extension':
        if len(sys.argv) != 5:
            print("Usage: python main.py --extension <file1> <file2> <output_file>")
            sys.exit(1)
        
        file1 = sys.argv[2]
        file2 = sys.argv[3]
        output_file = sys.argv[4]
        
        print("====================================")
        print("Starting Incremental Protein Search m8e file merger (extension mode)")
        print("------------------------------------")
        print(f"Input file 1: {file1}")
        print(f"Input file 2: {file2}")
        print(f"Output file: {output_file}")
        print("====================================\n")
        
        merge_m8e_files(file1, file2, output_file)
    
    else:
        print("Invalid mode. Use --default or --extension.")
        sys.exit(1)

if __name__ == "__main__":
    main()
