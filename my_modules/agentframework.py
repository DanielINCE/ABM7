# Import time
import time

# Import modules
import agentframework as af
import geometry.get_distance as ge

# Variables for constraining movement.
# The minimum x coordinate.
x_min = 0
# The minimum y coordinate.
y_min = 0
# The maximum x coordinate.
x_max = 99
# The maximum y coordinate.
y_max = 99

# Set the pseudo-random seed for reproducibility
import random
rn = random.random()
print(rn)
random.seed(0)

# Initialise variable x0
x0 = 0
print("x0", x0)

# Initialise variable y0
y0 = 0
print("y0", y0)

# Create a list to store agents
agents = []

# Create a class definition for an agent class
class Agent(object):
    pass
def __repr__(self):
    return str(self)

# A variable to store the number of agents
n_agents = 3

n_iterations = 10

# Initialise agents
agents = []
for i in range(n_agents):
    # Create an agent
    agents.append(af.Agent())
    print(agents[i])
print(agents)
  
# Add a constructor method to agent class
import random

class Agent(object):
    def __init__(self):
        self.x = random.randint(0, 99)
        self.y = random.randint(0, 99)
    def __init__(self, i):

        self.i = i
        self.x = random.randint(0, 99)
        self.y = random.randint(0, 99)
        def __getitem__(self, item):
            pass
        
# Define the method in the Agent class
def __str__(self):
    return self.__class__.__name__ + "(x=" + str(self.x) \
        + ", y=" + str(self.y) + ")"

# Define a method called 'move'
def move(self, x_min, y_min, x_max, y_max):
    for i in range(n_iterations):
    # Change agents[i] coordinates randomly
    # x-coordinate
        rn = random.random()
        #print("rn", rn)
        if rn < 0.5:
            agents[self].x = agents[self].x + 1
        else:
            agents[self].x = agents[self].x - 1
            # y-coordinate
            rn = random.random()
            #print("rn", rn)
            if rn < 0.5:
                agents[self].y = agents[self].y + 1
            else:
                agents[self].y = agents[self].y - 1
print(agents)

# Change x0 and y0 randomly
rn = random.random()
print("rn", rn)
if rn < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
print("x0", x0)
rn = random.random()
print("rn", rn)
if rn < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
print("y0", y0)

# Move agents

# Append to the list agents
agents.append([agents[0][0],agents[0][1]])

# Initialise variable x0
agents[0][0] = random.randint(0, 99)
print("agents[0][0]", agents[0][0])

# Initialise variable y0
agents[0][1] = random.randint(0, 99)
print("agents[0][1]", agents[0][1])
agents.append([agents[0][0], agents[0][1]])

# Set the pseudo-random seed for reproducibility
import random
rn = random.random()
print(rn)
random.seed(1)

# Initialise variable x1
x1 = 1
print("x1", x1)

# Initialise variable y1
y1 = 1
print("y1", y1)

# Change x1 and y1 randomly
if rn < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
x0 = 0
print("x0", x0)
y0 = 0
print("y0", y0)
x1 = 3
print("x1", x1)
y1 = 4
print("y1", y1)


# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
import math
def pythag(x,y):
    sum = x * x + y * y
    z = math.sqrt(sum)

    return(z)

(solution) = pythag(3,4)

print(solution)

import matplotlib.pyplot as plt
import operator

# Plot the agents
for i in range(n_agents):
    plt.scatter(agents[i].x, agents[i].y, color='black')
# Plot the coordinate with the largest x red
lx = min(agents, key=operator.itemgetter(0))
plt.scatter(lx.x, lx.y, color='red')
# Plot the coordinate with the smallest x blue
sx = min(agents, key=operator.itemgetter(0))
plt.scatter(sx.x, sx.y, color='blue')
# Plot the coordinate with the largest y yellow
ly = min(agents, key=operator.itemgetter(1))
plt.scatter(ly.x, ly.y, color='yellow')
# Plot the coordinate with the smallest y green
sy = min(agents, key=operator.itemgetter(1))
plt.scatter(sy.x, sy.y, color='green')
plt.show()

# Get the coordinates with the largest x-coordinate
print(max(agents, key=operator.itemgetter(0)))

# Define 'Get Distance'
def get_distance(x0, y0, x1, y1):
    
    
# Calculate the difference in the x coordinates.
    dx = x0 - x1
    
# Calculate the difference in the y coordinates.
    dy = y0 - y1
    
# Return the Sum the squared differences square rooted.
    return ((dx * dx) + (dy * dy)) ** 0.5

# Set time variable
start = time.perf_counter()

# Initialise max_distance

max_distance = math.inf
for i in range(len(agents)):
    a = agents[i]
    for j in range(len(agents)):
        b = agents[j]
if i < j:
        distance = get_distance(a.x, a.y, b.x, b.y)
        print("distance between", a, b, distance)
        max_distance = max(max_distance, distance)
        print("max_distance", max_distance)

print("i", i, "j", j)

# calculate and report a time interval
end = time.perf_counter()
print("Time taken to calculate maximum distance", end - start, "seconds")

# Apply movement constraints.
if agents[i].x < x_min:
    agents[i].x = x_min
if agents[i].y < y_min:
    agents[i].y = y_min
if agents[i].x > x_max:
    agents[i].x = x_max
if agents[i].y > y_max:
    agents[i].y = y_max
    
# Define geometry
    
def share(self, neighbourhood):
    # Create a list of agents in neighbourhood
    neighbours = []
    #print(self.agents[self.i])
    for a in self.agents:
        distance = geometry.get_distance(a.x, a.y, self.x, self.y)
        if distance < neighbourhood:
            neighbours.append(a.i)
    # Calculate amount to share
    n_neighbours = len(neighbours)
    #print("n_neighbours", n_neighbours)
    shares = self.store / n_neighbours
    #print("shares", shares)
    # Add shares to store_shares
    for i in neighbours:
        self.agents[i].store_shares += shares