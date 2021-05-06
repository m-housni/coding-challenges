/*
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
N=1000
run: node fileName.js to check
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
function multiplesThreeFive(N) {

  let mThree = []
  let mFive = []
  let m = []

  // multiples of 3 smaller than N
  let i=1
  while (3 * i < N) {
    mThree.push(3 * i)
    i++
  }

  // multiples of 5 smaller than N
  let j=1
  while (5 * j < N) {
    mThree.push(5 * j)
    j++
  }

  m = mThree.concat(mFive).unique()

  return m.sum()
}

// run it node fileName.js
console.log(multiplesThreeFive(1000))