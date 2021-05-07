"""
* A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
* Find the largest palindrome m
numDigits 
N=3
[995, 583, 580085]
N=4
[9999, 9901, 99000099]
N=5
[99995, 58663, 5866006685]
"""

# number to array
def numToArray(num):
  numArr = []
  while num//10 != 0:
    numArr.append(num%10)
    num = num//10
  numArr.append(num%10)
  return numArr[::-1]


# is pelindrom
def isPelindrom(num):

  # num <= 99
  if num<=99:
    if num//10 == num % 10:
      return True
    else:
      return False

  # num >= 100
  numArr = numToArray(num)
  lastIndex = len(numArr)-1
  pelindrom = True
  for i in range(0,lastIndex//2+1):
    if numArr[i] != numArr[lastIndex-i]:
      pelindrom = False
      break
  return pelindrom

# pelindroms for numDigits=3
def pelindroms():
  min = 100
  max = 999
  pelindroms = []
  for i in range(min,max):
    for j in range(min,max):
      if isPelindrom(i*j):
        pelindroms.append(i*j)
  return pelindroms

# largest pelindrom for numDigits=3
def largestPelindromProduct3():
  min = 10**2
  max = 9*10**2+9*10**1+9*10**0
  pelindroms = []
  for i in range(max, min,-1):
    for j in range(max, min,-1):
      if isPelindrom(i*j):
        return [i,j,i*j]
  return 'No result'

## largest pelindrom for numDigits=N
def largestPelindromProductN(N):

  min = 10**(N-1)
  max = 0
  for p in range(N):
    max = max + 9*10**p
  
  pelindroms = []
  for i in range(max, min, -1):
    for j in range(max, min, -1):
      if isPelindrom(i*j):
        return [i, j, i*j]
  return 'No result'


print(largestPelindromProductN(5))

