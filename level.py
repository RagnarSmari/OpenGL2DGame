from OpenGL.GL import *
from OpenGL.GLU import *
from enemy import Enemy
from rectangle import Rectangle
from circle import Circle

class Level:
    def __init__(self) -> None:
        self.enemies = []
        self.enemy1 = Enemy(200,500, 40, [1.0, 0.0, 1.0])
        self.enemy2 = Enemy(700,600, 60, [1.0,0.0,1.0])
        self.enemies.append(self.enemy1)
        self.enemies.append(self.enemy2)

    def draw_level(self):
        # As this game is simple, only difference in levels will be the number of enemies
        # Draw the enemies here, initialize them in init, this is level0
        if self.enemy1.exists:
            self.enemy1.draw_enemy()
        if self.enemy2.exists:
            self.enemy2.draw_enemy()

