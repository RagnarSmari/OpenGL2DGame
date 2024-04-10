from rectangle import Rectangle
from OpenGL.GL import *
from OpenGL.GLU import *


# Player is gonna be made up of a rectangle and is only gonna be a rectangle which shoots on space
class Player:
    def __init__(self, x, y, color = [0,0,0]) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.shots = []
        self.isShooting = False
        self.moveLeft = False
        self.moveRight = False
        self.speed = 500

    def draw_player(self):
        glBegin(GL_QUADS)
        glColor3f(self.color[0], self.color[1], self.color[2])
        glVertex2f(self.x, self.y)
        glVertex2f(self.x, self.y+70)
        glVertex2f(self.x+35, self.y+70)
        glVertex2f(self.x+35, self.y)
        glEnd()