#!/bin/bash
# run all functions starting with "test_" from all the files starting with "test_" in "research_tests directory"
# -v verbose - what logs should be saved
# -n number of workers, for parallelization
pytest research_tests/ -v -n 5   -m preprocess      --html=../results/1-preprocess.html  --self-contained-html
pytest research_tests/ -v -n 5   -m experiments1    --html=../results/2-exp1.html        --self-contained-html
pytest research_tests/ -v -n 5   -m experiments2    --html=../results/3-exp2.html        --self-contained-html
pytest research_tests/ -v        -m cleanup
