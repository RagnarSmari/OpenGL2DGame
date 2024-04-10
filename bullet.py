from circle import Circle

class Bullet:
    def __init__(self, x, y, speed, radius, color=[0,0,0]) -> None:
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = radius
        self.color = color


    def draw_bullet(self):
        shot = Circle(self.x,self.y,self.radius, 32, self.color)
        shot.draw_circle()
