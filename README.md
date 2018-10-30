# h1b_analysis
## Purpose: analyze given h1b dataset, return Top 10 Occupations and Top 10 States for certified visa applications to two txt files.
## Folder Structure: 
The directory structure for your repo should look like this:
```
├── README.md 
├── run.sh
├── src
│   └──h1b_counting.py
├── input
│   └──h1b_input.csv
├── output
|   └── top_10_occupations.txt
|   └── top_10_states.txt
├── insight_testsuite
└── run_tests.sh
└── tests
└── test_1
|   ├── input
|   │   └── h1b_input.csv
|   |__ output
|   |   └── top_10_occupations.txt
|   |   └── top_10_states.txt
├── test_2
├── input
│   └── h1b_input.csv
|── output
|   |   └── top_10_occupations.txt
|   |   └── top_10_states.txt
├── test_3
├── input
│   └── h1b_input.csv
|── output
|   |   └── top_10_occupations.txt
|   |   └── top_10_states.txt
├── test_4
├── input
│   └── h1b_input.csv
|── output
|   |   └── top_10_occupations.txt
|   |   └── top_10_states.txt
├── test_5
├── input
│   └── h1b_input.csv
|── output
|   |   └── top_10_occupations.txt
|   |   └── top_10_states.txt
```
## test datasets introduction:
### Input dataset: 
test_1 is the given test (10 cases); 
for other test cases, I randomly choose 10,000 cases from the following large dataset: 
test_2, test_3, test_4 are generated from H1B_FY_2014.csv, H1B_FY_2015.csv, H1B_FY_2016.csv, downloaded from Google Drive, 
test_5 is generated from H1B_FY_2017.csv, converted from the .xlsx file provided the government website. 
### Ground truth:
I compared the results with the results I've got in Matlab. 

## h1b_counting.py functions and intro
### Module dependency:
I only used the standard Python modules (BTW, God knows how much I miss pandas!!!)

`os, argparse, ast, numpy, collections, pdb (for debug), cProfile (to test speed)`
### Inputs
It uses argparse to specify all inputs. 

Things you have to specify:
--parent_path: working directory
--filename: input filename
--visa_key: application status(case sensitive)
--state_key: column name for working state (case sensitive)
--soc_num_key: column name for soc code (case sensitive)
--soc_name_key: column name for soc name (case sensitive)

Things that normally unchanged: 
--header_idx: if True, the input file includes headers
--cell_delimiter: delimiter to seperate each column
--certified_str: string for certified h1b application
--num_top: # of top frequent items
--out_occu_fn: output occupation file name
--out_state_fn: output state file name
--input_path: input subpath
--output_path: output subpath
--headers_states: headers of states used for output
--headers_occ: headers of occ used for output
--print_parser: if True, print all parameters

### Output: 
It only returns True or False, all other outputs are printed on the screen (such as current process, error information,  and output folder).


### Functions introduction: 
```
├── compile_csv
|   └──compile all data from csv, return numpy.array
├── soc_num_name_mapping
|   └── mapping soc_code to names
|   └──in case there're some typo in names (such as space), one soc code may have several names, use the mode.
├── top_n_freq_items
|   └──the funtion to calculate top n frequent occupations and work states
│   └──occupation, use soc code (and map to soc name afterwards)
|   └──work state: use work states, instead of employer states; if there are two work states, use the first one.
|   └──return: 
|   |   └──res: [[OCCUPATION/STATES, NUMBER_CERTIFIED_APPLICATIONS, PERCENTAGE]]
|   |   └──ct: raw data, for all keys, the counts
├── txt_writer
│   └──write results to a text file, given data, filename, path, headers
│   └── return True/False
├── main
|   └── The main function to call each subfunctions.
|   └── input: Defined by FLAGS, if no, use the default values
|   └── return True/False
|   └── It will print out current process, any error information, for better debugging.
```


## Running instruction:
In terminal:
1. cd to `h1b_analysis/insight_testsuite` 
2. run `./run_tests.sh`. The command (includes all parameters) to run each input files are written in `run.sh`. 
3. `run.sh `: You can specify the visa_status, workesite_state, soc_name keys in `h1b_counting.py`, however, in `run.sh`, now it's default to:

`--visa_key='CASE_STATUS' --state_key='WORKSITE_STATE' --soc_num_key='SOC_CODE' --soc_name_key='SOC_NAME'`


## Future improvements:
1. Increase speed:
    The main bottleneck is when compiling from csv, the usage of line.split(delimiter). I tried to use multiprocessing (commented within `compile_csv`), but somehow, it's even slower... If time permitted, I will explore more on that...
2. data cleansing:
I didn't do too much except: replace all `"` , convert to UPPER cases, mapping soc_code with potential soc_name, However, I found that when compiling csv files, there are some cases that has larger length than the headers. Since I am using line.split(delimiter), I guess there might be other  `;` within the files that is not served as delimiter....So maybe a better data cleansing should be done...
3. parameter passing (headers):
Can it be automatic, to find headers in given datafiles, and look for relevant columns by keywords....
