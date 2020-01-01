# Area of a triangle with co-ordinates
# * Using formula from https://mathinstructor.net/2012/08/how-to-find-area-of-triangle-given-three-vertices/

def area(c1, c2, c3):
  return abs((c1[0] * (c2[1] - c3[1]) + c2[0] * (c3[1] - c1[1]) + c3[0] * (c1[1] - c2[1]))//2)

print(area((-3,4), (-2,-2), (3,2)))



