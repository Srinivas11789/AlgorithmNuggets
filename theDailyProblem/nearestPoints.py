"""
Given a list of points, an interger k, and a point p, find the k closest points to p.

Here's an example and some starter code:

class Point:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __repr__(self):
    return f"({self.x}, {self.y})"

def closest_points(points, k, p):
  # Fill this in.

points = [
    Point(0, 0),
    Point(1, 1),
    Point(2, 2),
    Point(3, 3),
]
print(closest_points(points, 2, Point(0, 2)))
# [(0, 0), (1, 1)]
"""

class Point:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __repr__(self):
    return str((self.x, self.y))

def distance(p1, p2):
  import math
  return math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)

def closest_points(points, k, p):
  points = sorted(points, key=lambda x: distance(x, p))
  return points[:k]

points = [
    Point(0, 0),
    Point(1, 1),
    Point(2, 2),
    Point(3, 3),
]
print(closest_points(points, 2, Point(0, 2)))
# [(0, 0), (1, 1)]

