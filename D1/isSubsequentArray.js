function isSubsequentArray(arr1, arr2) {
  // filter arr1
  filtred = arr1.filter(el => arr2.includes(el))
  console.log(filtred)
  if (isArraysEqual(filtred, arr2)) 
    return true
  return false
}

function isArraysEqual(arr1, arr2) {
  if (arr1.length != arr2.length) 
    return false
  else {
    let i = 0
    while (i < arr1.length && arr1[i] == arr2[i]) {
      i++
    }
    if (i == arr1.length ) 
      return true
    else
      return false
  }
}

console.log(isSubsequentArray([1,2,3,0,8],[1,3,8]))