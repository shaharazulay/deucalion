def partition(arr, begin, end):
	pivot_idx = begin

	for i in range(begin + 1, end + 1):

		if arr[i] <= arr[begin]:
			pivot_idx += 1
			arr[i], arr[pivot_idx] = arr[pivot_idx], arr[i]
	arr[pivot_idx], arr[begin] = arr[begin], arr[pivot_idx]

	return pivot_idx


def quick_sort_recursion(arr, begin, end):
	if begin >= end:
		return

	pivot_idx = partition(arr, begin, end)
	quick_sort_recursion(arr, begin, pivot_idx - 1)
	quick_sort_recursion(arr, pivot_idx + 1, end)


def quick_sort(array, begin=0, end=None):
	if end is None:
		end = len(array) - 1

	return quick_sort_recursion(array, begin, end)
