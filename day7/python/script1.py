def typeOfHand(hand):
    #given a set of 5 cards, get the type of hans (5 of a kind, 4 of a kind etc...)
    for card in hand:

        c = hand.count(card)

        if c == 5:
            hand = hand.replace(card, "")
            return 1

        elif c == 4:
            hand = hand.replace(card, "")
            return 2

        elif c == 3:
            hand = hand.replace(card, "")
            return 5 + typeOfHand(hand)

        elif c == 2:
            hand = hand.replace(card, "")
            return 10 + typeOfHand(hand)
        
    else: 
        return 0 if len(hand) < 5 else 30

#5 of a type:1
#4 of a type:2
#full house: 15 -> 3
#tris: 5
#double pair: 20 -> 10
#couple: 15
#high card: 30

with open("../input.txt", "r") as f:
    lines = f.readlines()

    hands= []

    for line in lines:
        hand, bid = line.strip().split(" ")[0], int(line.strip().split(" ")[1])

        rank = typeOfHand(hand) 
        if rank == 15:
            rank = 3
        elif rank == 20:
            rank = 7
        handInfo = {"hand":hand, "bid":bid, "rank": 3 if rank == 12 else rank }
        
        hands.append(handInfo)

    
    #sort for lower rank and, if equal, to the higher card in order from first
    #to last card (A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2)

    #dictionary to order the cards from first to last card (A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2)
    order = {"A": 1, "K": 2, "Q": 3, "J": 4, "T": 5, "9": 6, "8": 7, "7": 8, "6": 9, "5": 10, "4": 11, "3": 12, "2": 13}

    hands.sort(key=lambda x: (x["rank"], [order[card] for card in x["hand"]]), reverse=True)

    for i in range(len(hands)):
        print(hands[i])

    win, count = 0,1

    for hand in hands:
        win += (hand["bid"]*count)
        #print("bid:",hand["bid"], "rank:",count, "win:",hand["bid"]*count)
        count += 1


    print(win)