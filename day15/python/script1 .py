def hashFun(letter, prev):
    return ((ord(letter) + prev)*17)%256

tot = 0

with open("../input.txt", "r") as f:
    data = f.read()

    data = data.split(",")

    for str in data:
        current = 0
        for i in range(len(str)):
            current = hashFun(str[i], current)
        tot += current

print(tot)