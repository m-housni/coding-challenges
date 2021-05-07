
/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

n=20
Result: 232792560

test
----
> tsc fileName.ts && node fileName.js

*/

export {} // to prevent duplicate function implementation error

function smallestMultiple(n: number): number {
  let found = false
  let p = 1
  let ctr = 0
  while (!found) {
    ctr = 0
    for (var i = 1; i <= n; i++) {
      if ((p * n) % i == 0) {
        ctr++
      }
    }
    if (ctr == n) {
      found = true
      return p * n
    }
    else {
      found = false
      p++
    }
  }
  return 0
}

console.log(smallestMultiple(23))