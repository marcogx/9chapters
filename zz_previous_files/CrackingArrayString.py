def reverse_arr(a, start, end):
	while start < end:
		a[start], a[end] = a[end], a[start]
		start += 1
		end -= 1


def mergesort(a):
	if not a:
		return
	helper = [0] * len(a)
	msort(a, helper, 0, len(a) - 1)


def msort(a, helper, start, end):
	if start < end:
		mid = start + (end - start) / 2
		msort(a, helper, start, mid)
		msort(a, helper, mid + 1, end)
		merge_arr(a, helper, start, mid, end)


def merge_arr(a, helper, start, mid, end):
	for i in xrange(start, end + 1):
		helper[i] = a[i]

	i, j, cur = start, mid + 1, start
	while i <= mid and j <= end:
		if helper[i] < helper[j]:
			a[cur] = helper[i]
			i += 1
		else:
			a[cur] = helper[j]
			j += 1
		cur += 1
	# right part is already there
	while i <= mid:
		a[cur] = helper[i]
		i += 1
		cur += 1


def insertionsort(a):
	if not a:
		return
	for i in xrange(1, len(a)):
		while i > 0 and a[i - 1] > a[i]:
			a[i - 1], a[i] = a[i], a[i - 1]
			i -= 1


def main():
	intervals = [[float('-inf'), float('inf')],[1,2],[4,7], [1,9]]
	inters = sorted(intervals, key=lambda x: x[1])
	print inters
	a1 = [5, 2, 9, 1, 5, 0]
	print a1
	# insertionsort(a1)
	mergesort(a1)
	print a1
	print

	a1 = [9, 7, 6, 5, 4, 2, 11]
	print a1
	# insertionsort(a1)
	mergesort(a1)
	print a1
	print

if __name__ == '__main__':
	main()