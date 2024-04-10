import math

class Collision:
    def __init__(self) -> None:
        pass

    def get_distance(self,obj1, obj2):
        xDistance = obj2.x - obj1.x
        yDistance = obj2.y - obj1.y
        return math.sqrt(math.pow(xDistance, 2) + math.pow(yDistance, 2))

    def circle_and_circle(self,obj1, obj2):
        if self.get_distance(obj1, obj2) < obj1.radius + obj2.radius:
            return True
        
        return False
    

    def circle_and_box(self,circle, box):
        if self.get_distance(circle, box) < box.y + circle.radius + 10:
            return True
        return False
