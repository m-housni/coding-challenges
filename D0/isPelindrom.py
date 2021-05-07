# example pelindroms: 121, 33, 3223, 435534

# is pelindrom
def isPelindrom(num):

  # num <= 99
  if num <= 99:
    if num//10 == num % 10:
      return True
    else:
      return False

  # num >= 100
  numArr = numberToArray(num)
  lastIndex = len(numArr)-1
  pelindrom = True
  for i in range(0, lastIndex//2+1):
    if numArr[i] != numArr[lastIndex-i]:
      pelindrom = False
      break
  return pelindrom
