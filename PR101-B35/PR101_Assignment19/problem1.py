# Write a function named distance that takes the x and y coordinates of two points and returns the distance between them.
# Sample Input: (2, 3), (5, 7);
# Sample Output: 5.0

import math

def distance(x1, y1, x2, y2):
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


print(distance(2, 3, 5, 7))
