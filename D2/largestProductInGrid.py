
"""
* In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
* ![grid](https: // github.com/m-housni/coding-challenges/blob/main/files/grid.jpg "grid")
* The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
* What is the greatest product of four adjacent numbers in the same direction(up, down, left, right, or diagonally) in the 20×20 grid?
"""

import random
import numpy as np

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
  for i in range(0,len(grid)-n+1):
    product = 1
    for j in range(i,i+n):
      product *= grid[k][j]
    if product>lprod:
      lprod = product
  return lprod

# largest product of adjacent n numbers in a column k
def largestProductInCol(grid, n, k):
  lprod = 1
  for i in range(0,len(grid[0])-n+1):
    product = 1
    for j in range(i,i+n):
      product *= grid[j][k]
    if product>lprod:
      lprod = product
  return lprod


# extract diagonals from grid
def extractDiagonalsFromGrid(grid):

  diags = []
  rows = len(grid)
  cols = len(grid[0])
  indexRow = min([rows,cols])
  indexCol = max([rows, cols])

  if rows>cols:
    grid = np.array(grid).T
    print(grid)

  # j for row 
  # i for col
  # principal dial: 1,1 - 2,2 - i,i === i=0,lastIndex

  for j in range(0,indexRow):
    diag = []
    for i in range(0, indexRow-j):
      try:
        diag.append(grid[i+j][i])
      except:
        print('out of range '+[i+j, i])
      finally:
        continue
    diags.append(diag)
    # print(diag)

  for j in range(1, indexCol):
    diag = []
    for i in range(0, indexCol-j):
      try:
        diag.append(grid[i][j+i])
      except:
        print('out of range '+[i+j, i])
      finally:
        continue
    diags.append(diag)
    # print(diag)
  return diags

def extractAllDiagonalsFromGrid(grid):
  diags = []
  diags.append(extractDiagonalsFromGrid(grid))
  diags.append(extractDiagonalsFromGrid(reverseGrid(grid)))
  return diags

def reverseGrid(grid):
  rGrid = []
  for i in range(len(grid)-1,-1,-1):
    rGrid.append(grid[i])

  return rGrid
    
# largest product of adjacent n numbers in a diagonal k
def largestProductInDiag(grid,n):
  diags = extractAllDiagonalsFromGrid(grid)
  lprod = 1
  for i in range(0,1):
    for j in range(0,len(diags[i])):
      product = 1
      for k in range(0,len(diags[i][j])):
        if len(diags[i][j])==n:
          product *= diags[i][j][k]
      if product>lprod:
        lprod = product

  return lprod

def largestProductInGrid(grid,n):

  pDiag = largestProductInDiag(grid, n)

  pCol = 1
  for i in range(0,len(grid)):
    if largestProductInCol(grid, n, i) > pCol:
      pCol = largestProductInCol(grid, n, i)

  pRow = 1
  for j in range(0, len(grid[0])):
    if largestProductInRow(grid, n, j) > pRow:
      pRow = largestProductInRow(grid, n, j)

  theLargest = [pDiag,pRow,pCol]

  return max(theLargest)


print(largestProductInGrid(createGrid(10, 10), 4))
