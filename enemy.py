from character import *

class enemy(character):
    def __init__(self, name, hp, str):
        character.__init__(name, hp)
        self.str = str
