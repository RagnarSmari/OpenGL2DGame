from OpenGL.GL import *
from OpenGL.GLU import *
import math


class Circle:
    def __init__(self, x, y, radius, sides, color = [0,0,0]) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.sides = sides
        self.color = color
    

    def draw_circle(self): 
        radius = self.radius    
        glColor3f(self.color[0], self.color[1], self.color[2])

        glBegin(GL_POLYGON)    
        for i in range(100):    
            cosine= radius * math.cos(i*2*math.pi/self.sides) + self.x   
            sine  = radius * math.sin(i*2*math.pi/self.sides) + self.y  
            glVertex2f(cosine,sine)
        glEnd()