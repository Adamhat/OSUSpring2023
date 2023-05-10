#!/bin/bash

# Array of different sizes
array_sizes=(32 64 128 256 512 1024 2048 4096 8192)

# Filename
filename="all04.cpp"
executable="./all04"

# Loop over each size
for size in "${array_sizes[@]}"
do
    # Replace ARRAYSIZE value in the C++ file
    sed -i "s/#define ARRAYSIZE.*/#define ARRAYSIZE $size*$size/g" $filename

    # Compile the program with the new ARRAYSIZE
    g++ -fopenmp -o $executable $filename

    # Run the program
    echo "Running program with ARRAYSIZE = $size * $size"
    ./$executable
done
