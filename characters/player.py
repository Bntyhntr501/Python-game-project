from .characters import *

class Player(Character):
    def __init__(self, name, hp, str, int):
        Character.__init__(self, name, hp)
        self.str = str
        self.int = int
