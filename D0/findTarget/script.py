
import math

"""
Linear runtime: O(n)
algo: linear search
"""
def findTargetLinear(list,target):
  """
  Return index of target if exists or None if not
  """
  for i in range(0,len(list)):
    if(list[i]==target):
      return i
  return None

"""
Logarithmic runtime: O(log n )
algo: binary search
"""
def fintTargetLog(list,target):
  """
  Assuming list is sorted
  """
  first = 0
  last = len(list)-1
  while first<last:
    middle = math.floor((first+last)/2)
    if list[middle]>target:
      last = middle-1
    elif list[middle]<target:
      first = middle+1
  if list[first]==target:
    return first
  else:
    return None

"""
logarithmic space
algo: recursif
"""
def findTargetRec(list,target):


list = [1,2,3,4,5,6,7,8]
target = 3
print(fintTargetLog(list,target))
