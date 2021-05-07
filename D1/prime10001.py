"""
* By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
* What is the 10 001st prime number?

Result: 104743
"""

def isPrime(n):
  for i in range(2,n//2):
    if(n%i==0):
      return False
  return True

def nthPrime(N):

  num = 3
  nth = 2
  i = 0
  while(nth!=N):
    num += 2
    if isPrime(num):
      nth += 1
  
  return num

print(nthPrime(50))
