"""
* The sum of the squares of the first ten natural numbers is,1^2+2^2+...+10^2 = 385
* The square of the sum of the first ten natural numbers is, (1+2+...+10)^2 = 3025
* Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385=2640
* Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

N=100
Result: 25164150

"""

def sumSquareDiff(N):

  sumSquares = 0
  squareSum = 0

  for i in range(1,N+1):
    sumSquares += i**2
    squareSum += i
  
  return squareSum**2-sumSquares


print(sumSquareDiff(100))
