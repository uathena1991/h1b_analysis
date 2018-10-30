import os
# import sys
import argparse
import ast
import numpy as np
# import multiprocessing
# import matplotlib.pyplot as plt
from collections import Counter, defaultdict
import pdb
# import time
# import cProfile

parser = argparse.ArgumentParser(description="All parameters")

###################### Need to specify #####################

parser.add_argument('--parent_path', type = str,
					default = '/Volumes/DATA/GitHub/h1b_analysis/',
					help='Working path')

parser.add_argument('--filename', type=str, default='h1b_input.csv',
					help='input file name(including extension)')


parser.add_argument('--visa_key', type=str,
					default='STATUS',
					help='Application status (case sensitive)')


parser.add_argument('--state_key', type = str,
					default = 'LCA_CASE_WORKLOC1_STATE',
					help='Column name for working state (case sensitive)')


parser.add_argument('--soc_num_key', type=str, default='LCA_CASE_SOC_CODE',
				help='Column name for soc code (case sensitive)')

parser.add_argument('--soc_name_key', type=str, default='LCA_CASE_SOC_NAME',
				help='Column name for soc name (case sensitive)')


################################ Normally unchanged  ################################

parser.add_argument('--header_idx', type = ast.literal_eval, default = True,
					help='if True, the input file includes headers')

parser.add_argument('--cell_delimiter', type=str, default=';',
					help='Delimiter to seperate each column')

parser.add_argument('--certified_str', type=str, default='CERTIFIED',
					help='String for certified h1b application')

parser.add_argument('--num_top', type=int, default = 10,
					help='# of top frequent items')


parser.add_argument('--out_occu_fn', type = str, default = 'top_10_occupations.txt',
					help='Output occupation file name')
parser.add_argument('--out_state_fn', type = str, default = 'top_10_states.txt',
					help='Output state file name')

parser.add_argument('--input_path', type = str, default = 'input',
					help='Input subpath')
parser.add_argument('--output_path', type = str, default = 'output',
					help='Output subpath')

parser.add_argument('--headers_states', type = str, default = 'TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE',
					help='Headers of states used for output')

parser.add_argument('--headers_occ', type = str, default = 'TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE',
					help='Headers of occ used for output')

parser.add_argument('--print_parser', type = ast.literal_eval, default = True,
					help='if True, print all parameters')


# FLAGS, unparsed = parser.parse_known_args()
# if FLAGS.print_parser:
# 	print(FLAGS)
#



# def compile_csv(filename, path,  cell_delimiter =  ";", header_idx = True):
# 	"""
#   multi processing version (but it doesn't increase speed a lot...
# 	read csv file, and save it into a numpy matrix
# 	:params: filename: str, input file name, including extension
# 	:params: path: str, input path
# 	:params: cell_delimiter: str, delimiter to seperate each column, default if ';'
# 	:params: header_idx: bool, Whether the file contains header
#
# 	returns:
# 		res_succ: np.array, cases that match len(headers)
# 		headers: list, headers
# 		res_trouble: np.array, cases that does not match len(headers)
# 	"""
# 	def sub_process(cond, res):
# 		tmp_sub_res = [tt.split(cell_delimiter) for tt in tmp_res[int(cond[0]*len(tmp_res)):int(cond[1]*len(tmp_res))]]
# #         tmp_sub_res = [np.fromstring(tt, sep = cell_delimiter) for tt in tmp_res[int(cond[0]*len(tmp_res)):int(cond[1]*len(tmp_res))]]
# 		res += tmp_sub_res
# 		return
# 	res_succ, res_trouble = [], []
#
# 	file = open(os.path.join(path, filename))
# 	tmp_res = [line[:-1] for line in file]
# 	file.close()
# 	if header_idx:
# 		headers = tmp_res[0].split(cell_delimiter)
# 		tmp_res = tmp_res[1:]
# 	else:
# 		headers = []
# 	## multithreads to do line.split()
# 	manager = multiprocessing.Manager()
# 	res = manager.list()
# 	num_proc = multiprocessing.cpu_count()
# 	# num_proc = 16
# 	print(num_proc)
# 	p_list = []
# 	for i in range(num_proc):
# 		p_list.append(multiprocessing.Process(target=sub_process, args = ([i/num_proc, (i+1)/num_proc], res)))
# 		p_list[-1].start()
# 	for pp in p_list:
# 		pp.join()
#
# #     pdb.set_trace()
# 	res_succ = [x for x in res if len(x) == len(headers)]
# 	print("Filename: %s\nNumber of all cases: %d\nNumber of correct format cases: %d \nNumber of problematic cases: %d" %(filename, len(tmp_res) - int(header_idx), len(res_succ), len(tmp_res) - 1 - len(res_succ)))
# 	return np.array(res_succ), headers, np.array(res_trouble)
# # raw_data, headers, trouble_data = compile_csv('H1B_FY_2014.csv')
# cProfile.run("compile_csv('H1B_FY_2014.csv')")

def compile_csv(filename, path, cell_delimiter =  ";", header_idx = True):
	"""
	read csv file, and save it into a numpy matrix
	:params: filename: str, input file name, including extension
	:params: path: str, input path
	:params: cell_delimiter: str, delimiter to seperate each column, default if ';'
	:params: header_idx: bool, Whether the file contains header

	returns:
		res_succ: np.array, cases that match len(headers)
		headers: list, headers
		res_trouble: np.array, cases that does not match len(headers)
	"""
	res_succ, res_trouble = [], []
	file = open(os.path.join(path, filename))
	tmp_res = [line[:-1] for line in file]
	file.close()
	if header_idx:
		headers = tmp_res[0].replace('"', '').split(cell_delimiter)
		tmp_res = tmp_res[1:]
		res = [tt.replace('"', '').split(cell_delimiter) for tt in tmp_res]

	else:
		headers = []
		res = [tt.replace('"', '').split(cell_delimiter) for tt in tmp_res]
	res_succ = [x for x in res if len(x) == len(headers)]
	# res_trouble = list(set(res[1:]).difference(set(res_succ)))
	print("Filename: %s\nNumber of all cases: %d\nNumber of correct format cases: %d \nNumber of problematic cases: %d" %(filename, len(tmp_res), len(res_succ), len(tmp_res) - len(res_succ)))
	return np.array(res_succ), headers, np.array(res_trouble)


# def data_cleansing(raw_data, column_idx):
# 	"""
# 	just in case of: Case issue, capitalize all words
# 	return:  UPPER cases data, as np.array
# 	"""
# 	res = np.array([[x.upper() for x in y] for y in raw_data])
# 	return res

def soc_num_name_mapping(certified_data, top_socs, soc_num_col, soc_name_col):
	"""
	mapping between soc number and soc names
	:return:
	"""
	res = defaultdict()
	for ts in top_socs:
		soc_names, counts = np.unique(certified_data[certified_data[:, soc_num_col]==ts, soc_name_col], return_counts = True)
		res[ts] = soc_names[np.argmax(counts)]
	return res



def top_n_freq_items(certified_data, key_col_idx, num_tops = 10):
	"""
	:params: certified_data: np.array, input data (with 'CERTIFIED' status)
	:params: key_col_idx: int, states column idx
	:params: visa_col_idx: int, visa column idx
	:params: num_states: int, top num_states frequent states

	returns:
		res: [[OCCUPATION/STATES, NUMBER_CERTIFIED_APPLICATIONS, PERCENTAGE]]
		ct: raw data, for all keys, the counts
	"""
	## using numpy.unique -- slower than Counter....
	#     unique, counts = np.unique(certified_data[:,key_col_idx], return_counts=True)
	#     return unique[np.argsort(counts)][::-1][:num_states]

	## using counter
	ct = Counter()
	for st in certified_data[:, key_col_idx]:
		ct[st] += 1
	del ct['']
	total_sum = len(certified_data)
	top_items = sorted(ct.most_common(num_tops), key = lambda x:(-x[1], x[0]))
	# most common ones, and in case of tie, sort it in alphabet order
	res = [[x[0], x[1], round(x[1]/total_sum, 3)] for x in top_items] # top_occupations/states, number_certified_applications, percentage
	return res, ct




def txt_writer(data, filename, path, headers):
	"""
	write data to a file, return True if succeed, else False.
	"""
	try:
		with open(os.path.join(path, filename), 'w') as file:
			## write headers
			file.write(headers)
			file.write("\n")
			## write data
			for row in data:
				file.write("%s;%d;%1.1f%%\n" %(row[0], row[1], row[2]*100))
		file.close()
	except ValueError:
		print("ERROR")
		return False
	return True




def main(FLAGS):
	"""
	:return:
		True/False, success/failure
	"""
	## load data
	print("Loading data from .csv...\n")
	try:
		raw_data, headers, trouble_data = compile_csv(FLAGS.filename, os.path.join(FLAGS.parent_path, FLAGS.input_path), FLAGS.cell_delimiter, FLAGS.header_idx)
		print("Done!\n")
	except ValueError:
		print("ERROR! Failed to load data from .csv")
		return False
	## find visa column idx:
	print("Finding key columns (application_status, working_state, soc_code, soc_name)...\n")
	try:
		visa_column = headers.index(FLAGS.visa_key)
		state_column = headers.index(FLAGS.state_key)
		soc_num_column = headers.index(FLAGS.soc_num_key)
		soc_name_column = headers.index(FLAGS.soc_name_key)
	except ValueError:
		print("ERROR! No keywords found! Check your visa_key, state_key, soc_num_key, soc_name_key!!\n")
		print("HEADERS in DATA:\n", headers)
		print("Your keyword: %s, %s, %s" %(FLAGS.visa_key, FLAGS.state_key, FLAGS.soc_num_key, FLAGS.soc_name_key))
		return False
	print("Done!\n")
	## data cleansing (like upper case, space, extra "" in ''), now embedded in compile_csv ????
	## get certified data
	try:
		print("Calculating top %d states (working state) and occupations(based on soc code) within all certified cases...\n" %FLAGS.num_top)
		certified_data = raw_data[raw_data[:,visa_column] == FLAGS.certified_str]
		print('Total number of CERTIFIED application %d' %len(certified_data))
		## get top n frequent items
		top_states, all_states = top_n_freq_items(certified_data, state_column, FLAGS.num_top)
		top_soc_num, all_soc_num = top_n_freq_items(certified_data, soc_num_column, FLAGS.num_top)
		# convert soc code to soc names
		soc_mapping = soc_num_name_mapping(certified_data, [x[0] for x in top_soc_num], soc_num_column, soc_name_column)
		top_soc_names0 = [[soc_mapping[x[0]], x[1], x[2]] for x in top_soc_num]
		top_soc_names = sorted(top_soc_names0, key = lambda x:(-x[1],x[0]))
		print("Done!\n")
	except ValueError:
		print("ERROR! FAILED to get top %d frequent occupations and states!\n" %FLAGS.num_top)
		return False
	## write to txt files
	print("Writing results to txt files...\n")
	try:
		stat_states = txt_writer(top_states, FLAGS.out_state_fn, os.path.join(FLAGS.parent_path, FLAGS.output_path), FLAGS.headers_states)
		stat_occ = txt_writer(top_soc_names, FLAGS.out_occu_fn, os.path.join(FLAGS.parent_path, FLAGS.output_path), FLAGS.headers_occ)
		print("Done! Outputs are within %s\n" %os.path.join(FLAGS.parent_path, FLAGS.output_path))
		return stat_states and stat_occ
	except ValueError:
		print("ERROR! FAILED to write results to txt files!\n")
		return False



if __name__ == '__main__':
	FLAGS, unparsed = parser.parse_known_args()
	if FLAGS.print_parser:
		print(FLAGS)
	FLAGS.parent_path = os.getcwd()
	res_final = main(FLAGS)

	# test speed
	# cProfile.run("compile_csv('H1B_FY_2014.csv')")
	# cProfile.run("main('H1B_FY_2016.csv', parent_path, 'CASE_STATUS', 'EMPLOYER_STATE', 'SOC_NAME')")




