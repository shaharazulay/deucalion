import logging

from _3_sum import *
from _sort import *
from deucalion import get_records
from copy import deepcopy

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger()


def	update_records(recordings):
	for record in recordings:
		record['f_original_name'] = record['f_name']
		record['f_ptr'] = assign_proper_func_ptr(record['f_name'])
		del record["f_name"]


def	assign_proper_func_ptr(original_func_name):
	bug_func_to_demonstrate = f"{original_func_name}_with_bugs"
	logging.debug(f"Serching for {bug_func_to_demonstrate}")
	if bug_func_to_demonstrate in globals():
		_logger.debug(f"Func {bug_func_to_demonstrate} is a match!")
		return globals()[bug_func_to_demonstrate]

	return globals()[original_func_name]


def replay_and_verify(records):
	behaviour_changed = []
	for record in records:
		tested_result = record["f_ptr"](*record["original_args"], **record["original_kwargs"])
		if tested_result != record["output"]:
			record["test_result"] = deepcopy(tested_result)
			behaviour_changed.append(record)
	return behaviour_changed

if __name__ == '__main__':
	arr = [0, -1, 2, -3, 1]
	found = find_zero_sum_triplets(arr, n=len(arr), k=0)
	records = get_records()
	update_records(records)
	suspicious = replay_and_verify(records)
	for record in suspicious:
		logging.warning(f"Found different outcome. func name {record['f_original_name']} - original output: "
						f"{record['output']}, current output: {record['test_result']}")


