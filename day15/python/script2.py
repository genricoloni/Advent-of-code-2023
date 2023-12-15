from collections import deque as Deque

def hashFun(letter, prev):
    return ((ord(letter) + prev) * 17) % 256

def operation_for_dash(box, label):
    # pop, if exists, the element with label label form box box
    if len(boxes[box]) > 0:
        for i in range(len(boxes[box])):
            if boxes[box][i]["label"] == label:
                #remove that element
                boxes[box].remove(boxes[box][i])
                return

def operation_for_equal(box, label, string):
    # check if the label label is already in box box
    for i in range(len(boxes[box])):
        if boxes[box][i]["label"] == label:
            boxes[box][i]["value"] = string[-1]
            return
    else:
        # if not, insert in the head
        boxes[box].append({"label": label, "value": string[-1]})


boxes = [Deque() for _ in range(256)]

with open("../input.txt", "r") as f:
    data = f.read().split(",")


for str in data:
    current_box = 0
    label = ''
    for i in range(len(str)):
        if str[i].isalpha():
            label += str[i]
            current_box = hashFun(str[i], current_box)
        elif str[i] == "-":
            operation_for_dash(current_box, label)
        else:
            operation_for_equal(current_box, label, str.replace("=", " "))

# Rest of the code for lens focusing power calculation
tot = 0

for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        tot += (1 + i) * (1 + j) * int(boxes[i][j]["value"])

print(tot)