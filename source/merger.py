import Bio
from Bio import SeqIO
from Bio.Seq import Seq
import csv

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
    for alignment in merged:
        query_id = alignment[0]
        subject_id = alignment[1]
        pair = (query_id, subject_id)

        if pair not in seen_pairs:
            unique_alignments.append(alignment)
            seen_pairs.add(pair)

    return unique_alignments


def rescale_evalues_m8(alignments, part_db_len, full_db_len):  
    scaling_factor = float(full_db_len) / float(part_db_len)  
    for alignment in alignments:
        evalue = float(alignment[-2])
        rescaled_evalue = evalue * scaling_factor
        alignment[-2] = str(rescaled_evalue)  # save rescaled e-value in the list




# def merge_m8_files(file1, file2, output_file, db_len_dict):  # 수정됨: db_len_dict 파라미터 추가
#     records1 = get_m8_record(file1)
#     records2 = get_m8_record(file2)

#     # 데이터베이스 길이 정보 사용
#     part_db_len1 = db_len_dict[file1]  # 수정됨: 파일 1의 데이터베이스 길이
#     part_db_len2 = db_len_dict[file2]  # 수정됨: 파일 2의 데이터베이스 길이
#     full_db_len = part_db_len1 + part_db_len2  # 수정됨: 전체 데이터베이스 길이 계산

#     # e-value 재조정
#     rescale_evalues_m8(records1, part_db_len1, full_db_len)  # 수정됨: 파라미터 변경
#     rescale_evalues_m8(records2, part_db_len2, full_db_len)  # 수정됨: 파라미터 변경

#     # 레코드 병합 및 결과 출력
#     merged_records = merge_records_m8(records1, records2)
#     with open(output_file, 'w', newline='') as f:
#         writer = csv.writer(f, delimiter='\t')
#         for record in merged_records:
#             writer.writerow(record)
