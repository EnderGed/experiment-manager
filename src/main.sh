#!/bin/bash
# run all functions starting with "test_" from all the files starting with "test_" in "research_tests directory

# commandline argument with the list of available gpus
if [ "$1" != "" ]; then
  GPUS=$1
else
  # default gpus
  GPUS="0,1,2,3,4,5"
fi

# -v verbose - what logs should be saved
# -n number of workers, for parallelization
pytest research_tests/ -v -n 10  -m preprocess    --gpus=$GPUS  --html=../results/1-preprocess.html  --self-contained-html
pytest research_tests/ -v -n 6   -m experiments1  --gpus=$GPUS  --html=../results/2-exp1.html        --self-contained-html
pytest research_tests/ -v -n 1   -m experiments2  --gpus=$GPUS  --html=../results/3-exp2.html        --self-contained-html
pytest research_tests/ -v        -m cleanup       --gpus=$GPUS
