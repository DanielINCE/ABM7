# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 16:48:16 2023

@author: User
"""
# Create a list to store agents
agents = []

# A variable to store the number of agents
n_agents = 3

n_iterations = 100

import random
rn = random.random()
print(rn)
random.seed(0)

# Initialise agents
agents = []
for i in range(n_iterations):
    agents.append([random.randint(0, 99), random.randint(0, 99)])
print(agents)

# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
import math
def pythag(x,y):
    sum = x * x + y * y
    z = math.sqrt(sum)

    return(z)

(solution) = pythag(3,4)

print(solution)

# Define 'Get Distance'
def get_distance(x0, y0, x1, y1):
    
    
# Calculate the difference in the x coordinates.
    dx = x0 - x1
    
# Calculate the difference in the y coordinates.
    dy = y0 - y1
    
# Return the Sum the squared differences square rooted.
    return ((dx * dx) + (dy * dy)) ** 0.5

# Initialise min_distance

min_distance = math.inf
for i in range(len(agents)):
    a = agents[i]
    for j in range(len(agents)):
        b = agents[j]
if i < j:
        distance = get_distance(a[0], a[1], b[0], b[1])
        print("distance between", a, b, distance)
        min_distance = min(min_distance, distance)
        print("min_distance", min_distance)

print("i", i, "j", j)