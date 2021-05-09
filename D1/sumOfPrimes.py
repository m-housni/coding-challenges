"""
Summation of primes
* The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
* Find the sum of all the primes below two million.
* 
N=100000 
Result: 454396537
"""

# is given numpber prime ?
def isPrime(n):
  for i in range(2, n//2):
    if(n % i == 0):
      return False
  return True

# sum of primes less than 1000000
def sumOfPrimes(N):
  oddNum = 3
  sum = 2
  while oddNum<=N:
    if isPrime(oddNum):
      sum += oddNum
    oddNum += 2
  return sum

print(sumOfPrimes(100000))



