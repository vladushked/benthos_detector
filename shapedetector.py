# import the necessary packages
import cv2 as cv

class ShapeDetector:
    lines = 0
    triangles = 0
    squares = 0
    circles = 0

    def __init__(self):
        pass

    def detect(self, c):
        """initialize the shape name and approximate the contour"""
        shape = "undefined"
        peri = cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, 0.04 * peri, True)

        # if shape is a line, it will have 2 vertices
        if len(approx) == 2:
            shape = "line"
            self.lines += 1

        # if shape is a triangle, it will have 3 vertices
        elif len(approx) == 3:
            shape = "triangle"
            self.triangles += 1

        # if shape is a square, it will have 4 vertices
        elif len(approx) == 4:
            shape = "square"
            self.squares += 1

        # otherwise the shape is a circle
        else:
            shape = "circle"
            self.circles += 1

    def print_figures(self):
        print('Lines - ' + str(self.lines))
        print('Triangles - ' + str(self.triangles))
        print('Circles - ' + str(self.circles))
        print('Squares - ' + str(self.squares) + '\n')

