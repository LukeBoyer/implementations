# functional quicksort implementation

def exchange(i, j, nums): # todo pull this into a different file and reference (learn about modules)
	ii = nums[i]
	jj = nums[j]
	
	nums[i] = jj
	nums[j] = ii

def partition(nums, left, right):
	pivot = nums[right]
	i = left - 1 
	for j in range(left, right):
		if nums[j] <= pivot:
			i = i + 1
			exchange(i, j, nums)
	exchange(right, i + 1, nums)
	return i + 1

def quicksort(nums, left, right):
	if left < right:
		pivot = partition(nums, left, right)
		quicksort(nums, left, pivot - 1)
		quicksort(nums, pivot + 1, right)