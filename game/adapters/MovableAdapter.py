from game.game_actions.motions import Movable
from game.game_objects.UObject import UObject


class MovableAdapter(Movable):
    def __init__(self, obj: UObject):
        self.obj = obj
        
    def get_position(self):
        return self.obj.get_property("position")
    
    def set_position(self, new_value):
        self.obj.set_property("position", new_value)
    
    def get_velocity(self):
        return self.obj.get_property("velocity")
