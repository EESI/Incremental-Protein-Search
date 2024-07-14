#!/bin/bash

# print usage information
usage() {
    echo "Usage:"
    echo "  $0 --default <file1> <file2> <output_file> <part_db_len1> <part_db_len2>"
    echo "  $0 --extension <file1> <file2> <output_file>"
    exit 1
}

# check the number of arguments
if [ "$#" -lt 1 ]; then
    usage
fi

MODE=$1

# debug prints to check arguments count and values
echo "Number of arguments: $#"
echo "Arguments: $@"

if [ "$MODE" == "--default" ]; then
    if [ "$#" -ne 6 ]; then
        echo "Expected 6 arguments for --default mode, but got $#"
        usage
    fi
    FILE1=$2
    FILE2=$3
    OUTPUT_FILE=$4
    PART_DB_LEN1=$5
    PART_DB_LEN2=$6

    echo "===================================="
    echo "starting incremental protein search m8 file merger (default mode)"
    echo "------------------------------------"
    echo "input file 1: $FILE1"
    echo "input file 2: $FILE2"
    echo "output file: $OUTPUT_FILE"
    echo "database length for file 1: $PART_DB_LEN1"
    echo "database length for file 2: $PART_DB_LEN2"
    echo "===================================="

    # execute the Python script
    python3 source/main.py --default "$FILE1" "$FILE2" "$OUTPUT_FILE" "$PART_DB_LEN1" "$PART_DB_LEN2"

elif [ "$MODE" == "--extension" ]; then
    if [ "$#" -ne 4 ]; then
        echo "Expected 4 arguments for --extension mode, but got $#"
        usage
    fi
    FILE1=$2
    FILE2=$3
    OUTPUT_FILE=$4

    echo "===================================="
    echo "starting incremental protein search m8e file merger (extension mode)"
    echo "------------------------------------"
    echo "input file 1: $FILE1"
    echo "input file 2: $FILE2"
    echo "output file: $OUTPUT_FILE"
    echo "===================================="

    # execute the Python script
    python3 source/main.py --extension "$FILE1" "$FILE2" "$OUTPUT_FILE"

else
    echo "Invalid mode: $MODE"
    usage
fi
