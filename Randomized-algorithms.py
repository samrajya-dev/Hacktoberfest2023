def partition(array, start, end):
  pivot = array[end]
  i = start
  for j in range (start, end):
    if array[j] < pivot:
      array[i], array[j] = array[j], array[i]
      i = i+1
  array[i], array[end] = array[end], array[i]
  return i;

def QuickSort (array, start, end):
  if start < end:
    pivotelement = partition(array, start, end)
    QuickSort(array, start, pivotelement - 1)
    QuickSort(array, pivotelement + 1, end)

array=[23,11,43,22,34,42,1]
#print(len(array))
QuickSort(array, 0, len(array)-1)
print(array)
