import pygame

class player:
    def __init__(self, pos, max_health = 250, health = 250, speed = 400, dash_speed = 1000, dash_timer = 0.2, dash_cooldown = 0):
        self.pos = pos
        self.health = health
        self.speed = speed
        self.max_health = max_health
        self.dash_speed = dash_speed
        self.dash_timer = dash_timer
        self.dash_cooldown = dash_cooldown



    def resetSpeed(self):
        self.speed = 400