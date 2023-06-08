#!/bin/bash

start=1

end=10

for i in $(seq $start $end)
do
   echo "Running program with $i processors..."
   mpiexec -np $i fourier
done
