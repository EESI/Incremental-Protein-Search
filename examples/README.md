## Prerequisites: Git LFS Installation

This tutorial requires **Git LFS (Large File Storage)** to properly download example files from the repository.  
If Git LFS is not installed, some files in the `examples/` directory may not be available or may appear as placeholder text.

### Install Git LFS

If Git LFS is not installed, you can install it using `conda`:

```bash
conda install -c conda-forge git-lfs
```

### Initialize Git LFS in the Repository

After cloning the repository, you must run the following commands **from the root directory** to properly download the required files:

```bash
git lfs install
git lfs pull
```

These commands ensure that all example files, including those in the examples/ directory, are properly retrieved.
Running git lfs pull is essential, as Git LFS stores large files separately and only downloads them when explicitly requested.



### Alternative Download Option  

If you prefer, you can manually download the required files from the following link:  
[Google Drive](https://drive.google.com/drive/folders/12SUcbIlfDfh0tVNxh7crxiVo5pUpWvdy?usp=sharing)  or [zenodo](https://zenodo.org/records/14889774)

Download **`fasta_example1.fa`** and **`fasta_example2.fa`**, and place them in the `examples/` directory.



# Tutorial Example 1

This tutorial should be executed from the root directory.

First, calculate the length of the db (fasta file) using the following Python scripts:

```bash
python3 utils/fasta_length_calculator.py examples/fasta_example1.fa
python3 utils/fasta_length_calculator.py examples/fasta_example2.fa
```

The lengths will be displayed on the screen as shown below:
```
 examples/fasta_example1.fa
Total sequence length: 6205115

 examples/fasta_example2.fa
Total sequence length: 6211928
```

Using these lengths, run the merge function as follows:
```
./run_merge.sh --default examples/input_example1.m8 examples/input_example2.m8 examples/output_example.m8 6205115 6211928
```

This will generate the result file examples/output_example.m8.



# Tutorial Example 2

This example is for m8e format.

First, convert m8 format to m8e format using the following Python scripts:

```bash
python3 utils/m8_to_m8e_converter.py examples/input_example1.m8 examples/fasta_example1.fa examples/m8e_example1.m8e
python3 utils/m8_to_m8e_converter.py examples/input_example2.m8 examples/fasta_example2.fa examples/m8e_example2.m8e
```

Then, run the merge function as follows:
```
./run_merge.sh --extension examples/m8e_example1.m8e examples/m8e_example2.m8e examples/output_example.m8e
```

This will generate the result file examples/output_example.m8e.
