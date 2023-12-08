from collections import deque
import re
from math import lcm


with open("../input.txt", "r") as f:
    data = f.readlines()

# Extract nodes from the input file
nodes = [{"name": i.split("=")[0][:-1], "leftChild": i.split("=")[1].split(",")[0][2:], "rightChild": i.split("=")[1].split(",")[1][1:-1].replace(")", "")} for i in data[2:]]
# Sort nodes by name

# Initialize deque and starting name
q = deque(data[0].strip())
name = 'AAA'
count = 0

regex = re.compile('..A')
startingNodes = [node["name"] for node in nodes if regex.match(node["name"])]

regex = re.compile('..Z')
destinationNodes = [node["name"] for node in nodes if regex.match(node["name"])]



counts = []

#starts with the nodes which names ends with A
for startingNode in startingNodes:
    count = 0
    name = startingNode
    while not name in destinationNodes:
        node = next(node for node in nodes if node["name"] == name)

        # Pop the element from the left of the deque
        direction = q.popleft()
        name = node["leftChild"] if direction == "L" else node["rightChild"]

        # Append the popped element at the end of the deque
        q.append(direction)

        count += 1
    
    counts.append(count)
    
    

#print the lcm of counts
print(lcm(*counts))

