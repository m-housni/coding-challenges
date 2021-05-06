/*
* The prime factors of 13195 are 5, 7, 13 and 29.
* What is the largest prime factor of the number 600851475143 ?

a prime factor is only divisible by 1 and its self
*/


var primeNumbers = require('../datasets/prime_numbers_1000.json')

function largestPrimeFactor(N) {
  var primeFactors = []
  for (var i = 0; i < primeNumbers.length; i++) {
    do {
      if (N % primeNumbers[i]==0) {
        primeFactors.push(primeNumbers[i])
        N = N / primeNumbers[i]
      }
      else {
        break
      }
    }
    while(N>2)
  }
  return primeFactors
}

console.log(largestPrimeFactor(600851475143))
// result: [ 71, 839, 1471, 6857 ]

  
