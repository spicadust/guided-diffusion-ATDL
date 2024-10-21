#!/bin/bash

# Check if both arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <ref_batch> <sample_batch>"
    exit 1
fi

# Assign arguments to variables
ref_batch=$1
sample_batch=$2

# Run the evaluation script with the provided arguments
poetry run python evaluations/evaluator.py "$ref_batch" "$sample_batch"
