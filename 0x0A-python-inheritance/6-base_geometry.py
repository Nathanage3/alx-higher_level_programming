#!/usr/bin/python3
"""Module that has an empty base class BaseGeometry and empty class function
"""


class BaseGeometry:
    """Geometry Class
    """

    def area(self):
        """Calculates the area
            Returns:
                float: area
        """
        raise Exception("area() is not implemented")
