# Incremental-Protein-Search

We developed Incremental Protein Search highly inspired by iBlast(https://github.com/vtsynergy/iBLAST).  



## Usage example

### default mode

./run_merge.sh --default source/blastp_astral_scope_result2.m8 source/blastp_astral_scope_result3.m8 source/merge_blastp_astral_scope_result23.m8 6205115 6211928





### extension mode

./run_merge.sh --extension source/blastp_astral_scope_result2.m8e source/blastp_astral_scope_result3.m8e source/merge_blastp_astral_scope_result23.m8e



## Docker Hub  

$ docker pull comhyunwoo/incremental-protein-search:latest


$ docker run --rm -v /home/user/data:/app/data comhyunwoo/incremental-protein-search:latest --default /app/data/blastp_astral_scope_result2.m8 /app/data/blastp_astral_scope_result3.m8 /app/data/merge_blastp_astral_scope_result23.m8 6205115 6211928  


$ docker run --rm -v /home/user/data:/app/data comhyunwoo/incremental-protein-search:latest --extension /app/data/blastp_astral_scope_result2.m8e /app/data/blastp_astral_scope_result3.m8e /app/data/merge_blastp_astral_scope_result23.m8e  

## Singularity

$ singularity pull docker://comhyunwoo/incremental-protein-search:latest


$ singularity exec -B /home/user/data:/app/data incremental-protein-search_latest.sif /bin/bash -c "cd /app/Incremental-Protein-Search && ./run_merge.sh --default /app/data/blastp_astral_scope_result2.m8 /app/data/blastp_astral_scope_result3.m8 /app/data/merge_blastp_astral_scope_result23.m8 6205115 6211928"


$ singularity exec -B /home/user/data:/app/data incremental-protein-search_latest.sif /bin/bash -c "cd /app/Incremental-Protein-Search && ./run_merge.sh --extension /app/data/blastp_astral_scope_result2.m8e /app/data/blastp_astral_scope_result3.m8e /app/data/merge_blastp_astral_scope_result23.m8e"
