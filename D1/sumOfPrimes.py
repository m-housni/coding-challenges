"""
Summation of primes
* The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
* Find the sum of all the primes below two million.
* 
N=100000 
Result: 454396537
N=2000000
Result: 142913828922

if n =  pxq 
p<q
p2<pq
p2<n
p<Vn

example 
6=3x2  => 2<V6
9=3x3 => 3<V9
26=2x13 => 2<V26

"""
import math

# is given numpber prime ?
def isPrime(n):
  for i in range(2, math.ceil(math.sqrt(n))+1):
    if(n % i == 0):
      return False
  return True

# sum of primes less than N
def sumOfPrimes(N):
  oddNum = 3
  sum = 2
  while oddNum<=N:
    if isPrime(oddNum):
      sum += oddNum
    oddNum += 2
  return sum


print(sumOfPrimes(100000))



