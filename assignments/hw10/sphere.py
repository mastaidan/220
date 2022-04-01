"""Contains the class called Sphere"""
from math import pi


class Sphere:
    """The Sphere class contains the object sphere which has radius as an instance variable. It also contains
methods that help in calculating parts of a sphere using radius, e.g. Volume"""

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def surface_area(self):
        return 4 * pi * self.radius * self.radius

    def volume(self):
        return 4 * pi * self.radius * self.radius * self.radius / 3
