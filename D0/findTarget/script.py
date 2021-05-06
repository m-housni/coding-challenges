
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
algo: recursif
test not passed
"""
def findTargetRec(list,target,left,right):
  # find middle
  middle = (left+right)//2
  # check no more elements
  if left>right:
    return -1
  # check = taget
  if list[middle]==target:
    return middle
  # recursive call: left to middle
  if list[middle]>target:
    findTargetRec(list,target,left,middle-1)
  # recursive call: middle to right
  if list[middle]<target:
    findTargetRec(list,target,middle+1,right)
  return -100

print(findTargetRec([1,2,3],3,0,2))
