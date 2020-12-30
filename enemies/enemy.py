import pygame


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 10
        self.path = []

    def draw(self):
        pass

    def collide(self):
        pass

    def move(self):
        pass

    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            return True
