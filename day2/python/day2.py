

#open the input
with open('../input.txt') as f:
    lines = f.readlines()

    tot = 0

    #create the collection to check
    toCheck = { "red" : 12,
                "green" : 13,
                "blue" : 14}

    for line in lines:
        #divide the line by ":"
        line = line.replace("\n","")
        line = line.split(":")
        id = line[0].split(" ")[1]

        sets = line[1].split(";")

        points = {  "red"   : 0,
                    "green" : 0,
                    "blue"  : 0}

        for s in sets:
            s.strip()
            extraction = s.split(",")
            for e in extraction:
                #remove the first char which is a space
                e = e[1:]
                e = e.split(" ")
                
                #check for the color
                if points[e[1]] < int(e[0]):
                    points[e[1]] = int(e[0])


        print("Minimum points for game", id, ":", points)
        tot += points["red"] * points["green"] * points["blue"]


    print(tot)
        



        


