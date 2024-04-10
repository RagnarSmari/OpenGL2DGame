from OpenGL.GL import *
from OpenGL.GLU import *

class Rectangle:
    def __init__(self, x, y, width, height, color=[0,0,0]) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw_rectangle(self):
        glBegin(GL_QUADS)
        glColor3f(self.color[0], self.color[1], self.color[2])

        # normal box
        glVertex2f(self.x, self.y)
        glVertex2f(self.x, self.y + self.height)
        glVertex2f(self.x + self.width, self.y + self.height)
        glVertex2f(self.x + self.width, self.y)
        glEnd()