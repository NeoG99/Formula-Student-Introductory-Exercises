import math
import pygame

class buildEnvironment:
    def __init__(self, MapDimensions):
        pygame.init()
        self.pointcloud = [] # Groups of 2D points in 2D-space
        self.externalMap = pygame.image.load("map1.png")
        self.maph, self.mapw = MapDimensions # Splits the canvas height and width
        self.MapWindowName = "RRT Path Planning"
        pygame.display.set_caption(self.MapWindowName)
        self.map = pygame.display.set_mode((self.mapw, self.maph)) # Specifies the map height and width to pygame
        # The above map is empty at first. We draw the image over with the following line:
        self.map.blit(self.externalMap, (0,0))
        # Colors
        self.black = (0,0,0)
        self.grey = (70,70,70)
        self.Blue = (0,0,255)
        self.Green = (0,255,0)
        self.Red = (255,0,0)
        self.white = (255,255,255)


