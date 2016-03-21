from character import *

class player(character):
    def __init__(self, name, hp, str, int):
        character.__init__(self, name, hp)
        self.str = str
        self.int = int
