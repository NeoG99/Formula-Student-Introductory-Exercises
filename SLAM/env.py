import math
import pygame
class buildEnvironment:
    def __init__(self,MapDimensions):
        pygame.init()
        self.pointCloud = [] # Groups of 2D points in 2D-space
        self.externalMap = pygame.image.load("map2.png")
        self.maph, self.mapw = MapDimensions # Splits the canvas height and width
        self.MapWindowName = "RRT Path Planning"
        pygame.display.set_caption(self.MapWindowName)
        self.map = pygame.display.set_mode((self.mapw, self.maph)) # Specifies the map height and width to pygame
        # The above map is empty at first. We draw the image over with the following line:
        self.map.blit(self.externalMap,(0,0))
        # Colors
        self.black = (0,0,0)
        self.grey = (70,70,70)
        self.Blue = (0,0,255)
        self.Green = (0,255,0)
        self.Red = (255,0,0)
        self.white = (255,255,255)

    def AD2pos(self, distance, angle, robotPosition):
        x = distance * math.cos(angle) + robotPosition[0]
        y = -distance * math.sin(angle) + robotPosition[1]
        return (int(x), int(y))

    def dataStorage(self, data):
        print(len(self.pointCloud))
        if data != False:
            for element in data:
                point = self.AD2pos(element[0], element[1], element[2])
                if point not in self.pointCloud:
                    self.pointCloud.append(point)

    def show_sensorData(self):
        self.infomap = self.map.copy()
        for point in self.pointCloud:
            self.infomap.set_at((int(point[0]), int(point[1])), (255,0,0))


