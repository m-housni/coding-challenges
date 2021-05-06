/*
If we list all the natural numbers below N that are multiples of p or q.
(?) Find the sum of all the multiples of p or q below N.
*/
 
// A modern JavaScript utility library delivering modularity, performance & extras.
var _ = require('lodash')

// the magic goes here
function multiplesPnQ(p,q,N) {

  let mP = []
  let mQ = []
  let m = []

  // multiples of p smaller than N
  let i=1
  while (p * i < N) {
    mP.push(p * i)
    i++
  }

  // multiples of q smaller than N
  let j=1
  while (q * j < N) {
    mQ.push(q * j)
    j++
  }

  m = _.union(mP,mQ)

  return _.sum(m)
}

// run it node fileName.js
var t1 = Date.now()
console.log('Result: '+multiplesPnQ(3, 4, 1000))
var t2 = Date.now()
console.log(t2-t1)