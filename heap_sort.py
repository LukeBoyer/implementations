# main client facing method

def heap_sort(*nums):
	return HeapSort(list(nums)).sort()

# helpers 

def parent(i):
	return i >> 1
	
def right(i):
	return (i + 1) * 2
	
def left(i):
	return ((i + 1) * 2) - 1 
		
def exchange(i, j, nums):
	ii = nums[i]
	jj = nums[j]
	
	nums[i] = jj
	nums[j] = ii
	
# implementation

class HeapSort:

	def __init__(self, nums):
		self.nums = nums
		self.heapsize = len(nums) - 1
		
	def build_heap(self):
		i = (len(self.nums) >> 1) - 1
		while i >= 0:
			self.max_heapify(i)
			i -= 1
		
	def max_heapify(self, i):
		l = left(i)
		r = right(i)
		largest = i
		
		if r <= self.heapsize and self.nums[r] > self.nums[largest]:
			largest = r
		if l <= self.heapsize and self.nums[l] > self.nums[largest]:
			largest = l
		
		if largest != i:
			exchange(i, largest, self.nums)
			self.max_heapify(largest)
			
	def sort(self):
		self.build_heap()
		for i in range(len(self.nums)):
			self.nums.append(self.nums.pop(0))
			self.heapsize -= 1
			self.max_heapify(0)
	
		return self.nums
			
			
	
			
	

			
			
			
		