import sys

import pygame
from pygame.locals import *

import math
import random

width = 400
height = 300

points = [
    [100, 200],
    [100, 250],
    [50, 200]
]
visited = []

density = 1/100

actors = [
    [10, 20], #Bert
    [30, 40]  #Elma
]

def init():
    pygame.init()
    global surface
    surface = pygame.display.set_mode((width, height), 0, 32)
    pygame.display.set_caption("bop")

def randP():
    return (random.randint(0, width), random.randint(0, height))

def setup():
    global actors
    global points
    global visited

    actors[0] = randP()
    actors[0] = randP()

    points = []
    visited = []
    while random.uniform(0, 1) > density:
        points.append(randP())

def dist(a, b):
    return math.sqrt((abs(a[0]-b[0])**2)+(abs(a[1]-b[1])**2))

def move(p):
    choice = 0
    i = 1
    while i < len(points):
        a = dist(points[choice], actors[p])
        b = dist(points[i], actors[p])
        if dist(points[choice], actors[p]) > dist(points[i], actors[p]):
            choice = i
        i+=1
    actors[p] = points[choice]
    visited.append(points.pop(choice))

def draw():
    surface.fill((32, 32, 32))

    for i, point in enumerate(points):
        pygame.draw.circle(surface, (128, 128, 224), (point[0], point[1]), 2)
        if i > 0:
            pygame.draw.line(surface, (128, 128, 224), (points[i-1][0], points[i-1][1]), (point[0], point[1]))

    for i, point in enumerate(visited):
        pygame.draw.circle(surface, (224, 128, 128), (point[0], point[1]), 2)
        if i > 0:
            pygame.draw.line(surface, (224, 128, 128), (visited[i-1][0], visited[i-1][1]), (point[0], point[1]))

    for point in actors:
        pygame.draw.circle(surface, (224, 224, 128), (point[0], point[1]), 2)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


def run():
    state = 0
    draw()
    while len(points) > 0:
        pygame.time.wait(100)
        move(state)
        draw()
        state = 0 if state else 1
    pygame.time.wait(10000)


if __name__ == '__main__':
    init()
    setup()
    run()



