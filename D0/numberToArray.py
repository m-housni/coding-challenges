# convert a number to an array

def numberToArray(num):
  numArr = []
  while num//10 != 0:
    numArr.append(num % 10)
    num = num//10
  numArr.append(num % 10)
  return numArr[::-1]
