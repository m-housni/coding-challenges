"""
*A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
*a2 + b2 = c2
*For example, 32 + 42 = 9 + 16 = 25 = 52.
*There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Result: 200, 375, 425
Product: 31875000
"""

def findTriplet():

  a = 3
  b = 4
  c = 5
  triplets = []
  for a in range(3,1000):
    for b in range(4, 1000):
      c = (a**2+b**2)**0.5
      if c.is_integer():
        triplets.append([a,b,c])
  
  for i in range(len(triplets)):
    if triplets[i][0]+triplets[i][1]+triplets[i][2] == 1000:
      product = triplets[i][0]*triplets[i][1]*triplets[i][2]
      return [triplets[i],product]


print(findTriplet())
