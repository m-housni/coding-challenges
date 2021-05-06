/*
If we list all the natural numbers below N that are multiples of p or q.
(?) Find the sum of all the multiples of p or q below N.
*/

  // unique values in array
  Array.prototype.unique = function() {
    var a = this.concat();
    for(var i=0; i<a.length; ++i) {
        for(var j=i+1; j<a.length; ++j) {
            if(a[i] === a[j])
                a.splice(j--, 1);
        }
    }
    return a;
  };

  // sum values of array
  Array.prototype.sum = function() {
    var a = this
    var sum = 0
    for (var i = 0; i < a.length; i++) {
      sum += a[i]
    }
    return sum
  };

// the magic goes here
function multiplesPnQ(p,q,N) {

  let mP = []
  let mQ = []
  let m = []

  // multiples of 3 smaller than N
  let i=1
  while (p * i < N) {
    mP.push(p * i)
    i++
  }

  // multiples of 5 smaller than N
  let j=1
  while (q * j < N) {
    mQ.push(q * j)
    j++
  }

  m = mP.concat(mQ).unique()

  return m.sum()
}

// run it node fileName.js
var t1 = Date.now()
console.log('Result: '+multiplesPnQ(3, 4, 100000))
var t2 = Date.now()
console.log(t2-t1)