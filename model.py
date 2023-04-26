# Import modules
import imageio
import os
import my_modules.agentframework as af
import my_modules.io as io
import my_modules.geometry.get_distance as ge

# Import time
import time

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

# Include the agents list and add an attribute for storing the shares:
def __init__(self, agents, i, environment, n_rows, n_cols):
    """
    The constructor method.

    Parameters
    ----------
    agents : List
        A list of Agent instances.
    i : Integer
        To be unique to each instance.
    environment : List
        A reference to a shared environment
    n_rows : Integer
        The number of rows in environment.
    n_cols : Integer
        The number of columns in environment.

    Returns
    -------
    None.

    """
    self.agents = agents
    self.i = i
    self.environment = environment
    tnc = int(n_cols / 3)
    self.x = random.randint(tnc - 1, (2 * tnc) - 1)
    tnr = int(n_rows / 3)
    self.y = random.randint(tnr - 1, (2 * tnr) - 1)
    self.store = 0
    self.store_shares = 0

# Create a list to store agents
agents = []

# A variable to store the number of agents
n_agents = 3

n_iterations = 100

# Initialise agents
agents = []
for i in range(n_iterations):
    agents.append([random.randint(0, 99), random.randint(0, 99)])
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
for i in range(n_iterations):
    # Change agents[i] coordinates randomly
    # x-coordinate
    rn = random.random()
    #print("rn", rn)
    if rn < 0.5:
        agents[i][0] = agents[i][0] + 1
    else:
        agents[i][0] = agents[i][0] - 1
    # y-coordinate
    rn = random.random()
    #print("rn", rn)
    if rn < 0.5:
        agents[i][1] = agents[i][1] + 1
    else:
        agents[i][1] = agents[i][1] - 1
print(agents)
    
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

import matplotlib.pyplot as plt
import operator

# Plot the agents
for i in range(n_agents):
    plt.scatter(agents[i][0], agents[i][1], color='black')
# Plot the coordinate with the largest x red
lx = min(agents, key=operator.itemgetter(0))
plt.scatter(lx[0], lx[1], color='red')
# Plot the coordinate with the smallest x blue
sx = min(agents, key=operator.itemgetter(0))
plt.scatter(sx[0], sx[1], color='blue')
# Plot the coordinate with the largest y yellow
ly = min(agents, key=operator.itemgetter(1))
plt.scatter(ly[0], ly[1], color='yellow')
# Plot the coordinate with the smallest y green
sy = min(agents, key=operator.itemgetter(1))
plt.scatter(sy[0], sy[1], color='green')
plt.show()

# Get the coordinates with the largest x-coordinate
print(max(agents, key=operator.itemgetter(0)))


# Set time variable
start = time.perf_counter()

# calculate and report a time interval
end = time.perf_counter()
print("Time taken to calculate maximum distance", end - start, "seconds")

# Apply movement constraints.
if agents[i][0] < x_min:
    agents[i][0] = x_min
if agents[i][1] < y_min:
    agents[i][1] = y_min
if agents[i][0] > x_max:
    agents[i][0] = x_max
if agents[i][1] > y_max:
    agents[i][1] = y_max
    
# Create directory to write images to.
    try:
        os.makedirs('../../data/output/images/')
    except FileExistsError:
        print("path exists")

    # For storing images
    global ite
    ite = 1
    images = []
    
# Main simulation loop
for ite in range(1, n_iterations + 1):
    print("Iteration", ite)
    # Move agents
    print("Move")
    for i in range(n_agents):
        agents[i].move(x_min, y_min, x_max, y_max)
        agents[i].eat()
        #print(agents[i])
    # Share store
    # Distribute shares
    for i in range(n_agents):
        agents[i].share(neighbourhood)
    # Add store_shares to store and set store_shares back to zero
    for i in range(n_agents):
        print(agents[i])
        agents[i].store = agents[i].store_shares
        agents[i].store_shares = 0
    print(agents)
    
    # Print the maximum distance between all the agents
    print("Maximum distance between all the agents", get_max_distance())
    # Print the total amount of resource
    sum_as = sum_agent_stores()
    print("sum_agent_stores", sum_as)
    sum_e = sum_environment()
    print("sum_environment", sum_e)
    print("total resource", (sum_as + sum_e))
    
# Plot environment
filename = '../../data/output/images/image' + str(ite) + '.png'
#filename = '../../data/output/images/image' + str(ite) + '.gif'
plt.savefig(filename)
plt.show()
plt.close()
images.append(imageio.imread(filename))

# Turn images into animated GIF
imageio.mimsave('../../data/output/out.gif', images, fps=3)

# initialise 'x_max' 
x_max = n_cols - 1
    
# initialise 'y_max' 
y_max = n_rows - 1

# Flip the y-axis
plt.ylim(y_max / 3, y_max * 2 / 3)
plt.xlim(x_max / 3, x_max * 2 / 3)

# Initialise Agents
def __init__(self, i, n_rows, n_cols):
    """
    The constructor method.

    Parameters
    ----------
    i : Integer
        To be unique to each instance.
    n_rows : Integer
        The number of rows in environment.
    n_cols : Integer
        The number of columns in environment.
    Returns
    -------
    None.
    """
    self.i = i
    tnc = int(n_cols / 3)
    self.x = random.randint(tnc - 1, (2 * tnc) - 1)
    tnr = int(n_rows / 3)
    self.y = random.randint(tnr - 1, (2 * tnr) - 1)


# Define Agents
def __init__(self, i, environment, n_rows, n_cols):
    """
    The constructor method.

    Parameters
    ----------
    i : Integer
    To be unique to each instance.
    environment : List
    A reference to a shared environment
    n_rows : Integer
    The number of rows in environment.
    n_cols : Integer
    The number of columns in environment.

    Returns
    -------
    None.

    """
self.i = i
self.environment = environment
tnc = int(n_cols / 3)
self.x = random.randint(tnc - 1, (2 * tnc) - 1)
tnr = int(n_rows / 3)
self.y = random.randint(tnr - 1, (2 * tnr) - 1)
self.store = 0

# Agent class
def eat(self):
    if self.environment[self.y][self.x] >= 10:
        self.environment[self.y][self.x] -= 10
        self.store += 10