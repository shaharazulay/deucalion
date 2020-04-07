from _3_sum import find_zero_sum_triplets


if __name__ == '__main__':
	arr = [0, -1, 2, -3, 1]
	found = find_zero_sum_triplets(arr, n=len(arr), k=0)
	print(found)