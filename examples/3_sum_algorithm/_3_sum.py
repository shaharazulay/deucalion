from recursive_decorator import recursive_decorator

from deucalion import collector
from _sort import quick_sort


@recursive_decorator(collector)
def find_zero_sum_triplets(arr, n, k):
	found = []
	quick_sort(arr)

	for i in range(0, n - 1):

		l = i + 1
		r = n - 1
		x = arr[i]

		while l < r:

			if x + arr[l] + arr[r] == k:
				found.append((x, arr[l], arr[r]))
				l += 1
				r -= 1

			elif x + arr[l] + arr[r] < k:
				l += 1

			else:
				r -= 1

	return found
