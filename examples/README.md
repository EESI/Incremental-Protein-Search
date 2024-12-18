# Tutorial Example 1

This tutorial should be executed from the root directory.

First, calculate the length of the db (fasta file) using the following Python scripts:

```bash
python3 utils/fasta_length_calculator.py examples/fasta_example2.fa
python3 utils/fasta_length_calculator.py examples/fasta_example1.fa
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
