#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python
#
#python ./src/h1b_counting.py ./input/h1b_input.csv ./output/top_10_occupations.txt ./output/top_10_states.txt

## for given test_1
echo "Actual TEST running: $1"
case $1 in
  'test_1') python3 ./src/h1b_counting.py --parent_path='/Volumes/Data/GitHub/h1b_analysis/' --filename='h1b_input.csv' --visa_key='CASE_STATUS' --state_key='WORKSITE_STATE' --soc_num_key='SOC_CODE' --soc_name_key='SOC_NAME'
;;
#
### for test_2 h1b_FY_2014.csv
 'test_2') python3 ./src/h1b_counting.py --parent_path='/Volumes/Data/GitHub/h1b_analysis/' --filename='h1b_input.csv' --visa_key='STATUS' --state_key='LCA_CASE_WORKLOC1_STATE' --soc_num_key='LCA_CASE_SOC_CODE' --soc_name_key='LCA_CASE_SOC_NAME';;
#
###  for test_3 h1b_FY_2015.csv
 'test_3') python3 ./src/h1b_counting.py --parent_path='/Volumes/Data/GitHub/h1b_analysis/' --filename='h1b_input.csv' --visa_key='CASE_STATUS' --state_key='WORKSITE_STATE' --soc_num_key='SOC_CODE' --soc_name_key='SOC_NAME';;
##
### for  test_4 h1b_FY_2016.csv
    'test_4') python3 ./src/h1b_counting.py --parent_path='/Volumes/Data/GitHub/h1b_analysis/' --filename='h1b_input.csv' --visa_key='CASE_STATUS' --state_key='WORKSITE_STATE' --soc_num_key='SOC_CODE' --soc_name_key='SOC_NAME';;
##
###  for test_5 h1b_FY_2017.csv
 'test_5') python3 ./src/h1b_counting.py --parent_path='/Volumes/Data/GitHub/h1b_analysis/' --filename='h1b_input.csv' --visa_key='CASE_STATUS' --state_key='WORKSITE_STATE' --soc_num_key='SOC_CODE' --soc_name_key='SOC_NAME';;
esac
#
#


