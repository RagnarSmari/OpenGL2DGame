from circle import Circle

# Enemies in this game are only gonna be a circle
class Enemy:
    def __init__(self, x, y, radius, color = [0,0,0]) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mov_speed_x = 500
        self.mov_speed_y = 500
        self.exists = True


    def draw_enemy(self):
        circle = Circle(self.x,self.y,self.radius, 30,self.color)
        circle.draw_circle()



