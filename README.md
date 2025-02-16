# iSeqSearch: Incremental Protein Search for iBlast/iMMSeqs2/iDiamond  

We developed Incremental Protein Search highly inspired by iBlast(https://github.com/vtsynergy/iBLAST).  


# Overview 

Incremental Protein Search is a tool designed to merge protein search results. It operates in two modes: default and extension, supporting .m8 and .m8e files respectively. The tool can be run locally, via Docker, or using Singularity.

To view a tutorial example, please visit the following link:

[https://github.com/EESI/Incremental-Protein-Search/tree/main/examples](https://github.com/EESI/Incremental-Protein-Search/tree/main/examples)

## Requirements

To run this project, ensure that the following dependencies are installed:

- **Python**: Version 3.8 or higher
- **Biopython**: Version 1.79 (for sequence handling)
- **NumPy**: Version 1.21.0 (for numerical computations)
- **tqdm**: Version 4.64.0 (for progress bar display)


## Usage  

```bash
Usage: ./run_merge.sh [MODE] [INPUT_FILE1] [INPUT_FILE2] [OUTPUT_FILE] [DEFAULT_MODE_PARAMETERS]

Modes:
  --default    Use default mode for .m8 files
  --extension  Use extension mode for .m8e files

Arguments:
  INPUT_FILE1  Path to the first input file
  INPUT_FILE2  Path to the second input file
  OUTPUT_FILE  Path to the output merged file

Parameters Applicable Only to Default Mode:
  PARAM1       First integer parameter (e.g., sequence length of the first input file)
  PARAM2       Second integer parameter (e.g., sequence length of the second input file)
```

## Utils  

### Calculating DB length(get FASTA file size)

```
$ python utils/fasta_length_calculator.py <fasta_file_path>

```


## Usage example

### default mode

```
$ ./run_merge.sh --default source/blastp_astral_scope_result2.m8 source/blastp_astral_scope_result3.m8 source/merge_blastp_astral_scope_result23.m8 6205115 6211928
```




### extension mode

```
$ ./run_merge.sh --extension source/blastp_astral_scope_result2.m8e source/blastp_astral_scope_result3.m8e source/merge_blastp_astral_scope_result23.m8e
```


## Docker Hub  
```
$ docker pull comhyunwoo/incremental-protein-search:latest


$ docker run --rm -v "$(pwd)":/app -w /app comhyunwoo/incremental-protein-search:latest     --default /app/examples/input_example1.m8 /app/examples/input_example2.m8 /app/examples/output_example.m8 6205115 6211928  


$ docker run --rm -v "$(pwd)":/app -w /app comhyunwoo/incremental-protein-search:latest     --extension /app/examples/m8e_example1.m8e /app/examples/m8e_example2.m8e /app/examples/output_example.m8e  
```


## Singularity

```
$ singularity pull docker://comhyunwoo/incremental-protein-search:latest


$ singularity exec -B "$(pwd)":/app incremental-protein-search_latest.sif \
    /bin/bash -c "cd /app && ./run_merge.sh --default /app/examples/input_example1.m8 /app/examples/input_example2.m8 /app/examples/output_example.m8 6205115 6211928"


$ singularity exec -B "$(pwd)":/app incremental-protein-search_latest.sif \
    /bin/bash -c "cd /app && ./run_merge.sh --extension /app/examples/m8e_example1.m8e /app/examples/m8e_example2.m8e /app/examples/output_example.m8e"
```






This tool is particularly useful in protein sequence analysis workflows, especially when dealing with large datasets. The incremental search approach can significantly improve efficiency in processing and analyzing protein data. Its flexibility in execution methods (local, Docker, Singularity) makes it adaptable to various computational environments, from personal workstations to high-performance computing clusters.
