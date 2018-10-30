#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python
#
#python ./src/h1b_counting.py ./input/h1b_input.csv ./output/top_10_occupations.txt ./output/top_10_states.txt

## for given test_1
 python3 ./src/h1b_counting.py --parent_path='/Volumes/Data/GitHub/h1b_analysis/' --filename='h1b_input.csv' --visa_key='CASE_STATUS' --state_key='WORKSITE_STATE' --soc_num_key='SOC_CODE' --soc_name_key='SOC_NAME'
