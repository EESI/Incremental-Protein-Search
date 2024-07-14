import Bio
from Bio import SeqIO
from Bio.Seq import Seq
import csv
from tqdm import tqdm

def get_m8_record(result_file):
    with open(result_file, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        records = [row for row in reader]
    return records




def merge_records_m8(records1, records2):
    # integrate two records
    merged = records1 + records2

    # sort based on e-values
    merged.sort(key=lambda x: float(x[-2]))

    # remove duplication (when the query_id is same as the subject_id)
    unique_alignments = []
    seen_pairs = set()
    #for alignment in merged: 
    for alignment in tqdm(merged, desc="Merging records", unit="record"):# applying tqdm
        query_id = alignment[0]
        subject_id = alignment[1]
        pair = (query_id, subject_id)

        if pair not in seen_pairs:
            unique_alignments.append(alignment)
            seen_pairs.add(pair)

    return unique_alignments



def rescale_evalues_m8(alignments, part_db_len, full_db_len):  
    scaling_factor = float(full_db_len) / float(part_db_len)  
    #for alignment in alignments: 
    for alignment in tqdm(alignments, desc="Rescaling e-values", unit="alignment"):# applying tqdm
        evalue = float(alignment[-2])
        rescaled_evalue = evalue * scaling_factor
        alignment[-2] = str(rescaled_evalue)  # save rescaled e-value in the list
        
        

def merge_m8_files(file1, file2, output_file, part_db_len1, part_db_len2):  
    records1 = get_m8_record(file1)
    records2 = get_m8_record(file2)

    # 
    #part_db_len1 = db_len_dict[file1]  #
    #part_db_len2 = db_len_dict[file2]  #
    full_db_len = part_db_len1 + part_db_len2  # merged file db length

    # e-value rescale
    rescale_evalues_m8(records1, part_db_len1, full_db_len)  # 
    rescale_evalues_m8(records2, part_db_len2, full_db_len)  # 

    # merge record and write file
    merged_records = merge_records_m8(records1, records2)
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        #for record in merged_records: 
        for record in tqdm(merged_records, desc="Writing merged records", unit="record"):#applying tqdm
            writer.writerow(record)

            

