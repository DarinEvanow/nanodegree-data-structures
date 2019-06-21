import heapq


# Wrapper for MinHeap functionality
class MinHeap(object):
    def __init__(self): self.h = []
    def heappush(self,x): heapq.heappush(self.h,x)
    def heappop(self): return heapq.heappop(self.h)
    def __getitem__(self,i): return self.h[i]
    def __len__(self): return len(self.h)


# Wrapper for a MaxHeapObj, which we have so we can leverage the built in heapq by negating our values so they act
# as a minheap in implementation, but a maxheap in practice
class MaxHeapObj(object):
  def __init__(self,val): self.val = val
  def __lt__(self,other): return self.val > other.val
  def __eq__(self,other): return self.val == other.val
  def __str__(self): return str(self.val)


# Wrapper for MaxHeap functionality
class MaxHeap(MinHeap):
    def heappush(self,x): heapq.heappush(self.h,MaxHeapObj(x))
    def heappop(self): return heapq.heappop(self.h).val
    def __getitem__(self,i): return self.h[i].val


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    max_heap = MaxHeap()
    for item in input_list:
        max_heap.heappush(item)

    first = []
    second = []
    while len(max_heap) is not 0:
        first.append(max_heap.heappop())
        if len(max_heap) is not 0:
            second.append(max_heap.heappop())

    first = int("".join(map(str, first)))
    second = int("".join(map(str, second)))

    return [first, second]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_case1 = [[1, 2, 3, 4, 5], [542, 31]]
test_case2 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case1)
test_function(test_case2)
