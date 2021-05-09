
"""
* In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
* ![grid](https: // github.com/m-housni/coding-challenges/blob/main/files/grid.jpg "grid")
* The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
* What is the greatest product of four adjacent numbers in the same direction(up, down, left, right, or diagonally) in the 20×20 grid?
"""

import random

# create a grid
def createGrid(n, p):
  rows, cols = (n, p)
  grid = []
  for i in range(rows):
      col = []
      for j in range(cols):
        col.append(random.randint(1, 9))
      grid.append(col)
      print(col)

  return grid

# largest product of adjacent n numbers in a row k
def largestProductInRow(grid,n,k):
  lprod = 1
  for i in range(len(grid[k])-n):
    product = 1
    for j in range(i,i+n):
      product *= grid[k][j]
    if product>lprod:
      lprod = product
  return lprod

# largest product of adjacent n numbers in a column k
def largestProductInCol(grid, n, k):
  lprod = 1
  for i in range(len(grid[0])-n):
    product = 1
    for j in range(i,i+n):
      product *= grid[j][k]
    if product>lprod:
      lprod = product
  return lprod


# n-uplets 
def extractNupletsFromGrid(grid,n):
  nuplets = []
  row = len(grid)
  cols = len(grid[0])
  #....
  return nuplets

# largest product of adjacent n numbers in a diagonal k
def largestProductInDiag(grid):
  nuplets = extractNupletsFromGrid(grid)
  lprod = 1
  for i in range(len(nuplets)):
    product = 1
    for j in range(len(nuplets[i])):
      product *= nuplets[i][j]
    if product>lprod:
      lprod = produit
  return lprod


print(largestProductInCol(createGrid(5,5),4,1))
