#script for the first part it's correct for the second one also, but it' pretty slow
#this script do the exactly same thing of the first one, but it's faster

with open("../input.txt") as f:
    lines = f.readlines()

    #for part2, just de comment next line
    lines = [line.replace(" ", "") for line in lines]
    times, distances = int(lines[0].split(":")[1].strip().split("   ")[0]), int(lines[1].split(":")[1].strip().split("   ")[0])  

c = 0

#for using the one-line (which is 0.2 s fastest)
for i in range(times):
    if i * (times - i) > distances:
        c = i
        break

print(times -2*c + 1) #+1 for the 'middle' element
#delete this cycle and the print just above

#as one line
# print((times - 2 * next(i for i in range(times) if i * (times - i) > distances)) + 1 if distances % 2 == 0 else (times - 2 * next(i for i in range(times) if i * (times - i) > distances) ))


