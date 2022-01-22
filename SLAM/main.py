import env
import sensors
import pygame
import math

environment = env.buildEnvironment((600, 1200))
running = True # Found in every pygame script

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update() # Updates the map
    