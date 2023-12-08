from collections import deque

with open("../input.txt", "r") as f:
    data = f.readlines()

# Extract nodes from the input file
nodes = [{"name": i.split("=")[0][:-1], "leftChild": i.split("=")[1].split(",")[0][2:], "rightChild": i.split("=")[1].split(",")[1][1:-1].replace(")", "")} for i in data[2:]]
# Sort nodes by name
nodes.sort(key=lambda x: x["name"])

# Initialize deque and starting name
q = deque(data[0].strip())
name = 'AAA'
count = 0

# Traverse the tree
while name != "ZZZ":
    node = next(node for node in nodes if node["name"] == name)
    
    # Pop the element from the left of the deque
    direction = q.popleft()
    name = node["leftChild"] if direction == "L" else node["rightChild"]
    
    # Append the popped element at the end of the deque
    q.append(direction)
    
    count += 1

print(count)
