"""Dummy challenge for Kitt Demo"""



def circle_area(radius):
    """Returns the area of the circle of given radius"""
    pi_number = 3.141592653589793
    area = radius**2*pi_number
    if radius <= 0:
        return 0
    return area
print(circle_area(4))
