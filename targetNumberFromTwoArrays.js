
/*
## Target number from two arrays
* example: given two arrays of same length:
* [-1,3,8,2,9,5]
* [4,1,2,10,5,20]
* and a target number like 24
* find two numbers one belongs to the 1st array, the second belongs the 2nd array whom sum is the closest to the target number
*
*/


//
function findNumbers(arr1, arr2, target) {

  let a1 = arr1.sort()
  let a2 = arr2.sort()
  let len = a1.length
  let grid = []
  let Nums = []

  // create grid of all possible sums
  for (var i = 0; i < len; i++) {
    let col = []
    for (var j = 0; j < len; j++) {
      col.push(a1[i] + a2[j])
    }
    grid.push(col)
    console.log(col)
  }

  // find Numbers
  let k = 0
  let l = 0
  let diff = Math.pow(10, 1000)
  for (j = len - 1 - k; j >= 0; j--) {
    for (i = l; i < len; i++) {
      if (grid[i][j] > target) {
        k++
      }
      else {
        l++
      }
      if (Math.abs(target - grid[i][j]) <= diff) {
        diff = Math.abs(target - grid[i][j])
        Nums = [a1[j], a2[i]]
        console.log([[j, i], Nums])
      }
    }
  }
  console.log(Nums)
}

// tested for positif arrays of integers
findNumbers([1,2,3,4,5],[2,3,5,8,13],20)
