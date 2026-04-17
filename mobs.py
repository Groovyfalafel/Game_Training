class mob:
    def __init__(self, pos, health = 100, speed = 200):
        self.pos = pos
        self.health = health
        self.speed = speed

    def setSpeed(self, speed):
        self.speed = speed