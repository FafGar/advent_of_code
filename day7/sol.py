cards = ('A','K','Q','J','T','9','8','7','6','5','4','3','2')
def quickSort(hands:list) -> list:
    if(len(hands) <= 1): return hands
    pivot = hands[0]
    lt = []
    gt = []
    for hand in hands:
        if hand[0] == pivot: continue
        for index in range(5):
            hand_val = cards.index(hand[0][index]) 
            pivot_val = cards.index(pivot[0][index])
            if hand_val > pivot_val:
                lt.append(hand)
                break
            elif hand_val < pivot_val:
                gt.append(hand)
                break
    return quickSort(lt)+[pivot]+quickSort(gt)
    
            


fin =  open('input.txt')
hands = [(line.split()[0],line.split()[1]) for line in fin.readlines()]



five_ok = []
four_ok = []
full_house = []
three_ok = []
two_pair = []
pair = []
high_card = []

for hand in hands:
    labels = set(hand[0])
    num_labels = len(labels)

    #Only one label: must be five of a kind
    if(num_labels == 1): five_ok.append(hand)
    # Only two labels: must be full house or 4 of a kind
    elif(num_labels == 2):
        #if any label occurs other than 1 or 4 times, must be a full house
        if(hand[0].count(hand[0][0]) not in (1,4)):
            full_house.append(hand)
        else:
            four_ok.append(hand)
    # 3 labels: must be 3 of a kind or two pair
    elif(num_labels == 3):
        #If there are two of any label, must be two pair
        if(2 in [hand[0].count(label) for label in labels]):
            two_pair.append(hand)
        else:
            three_ok.append(hand)
    elif(num_labels == 4):
        pair.append(hand)
    else:
        high_card.append(hand)


hand_lists = [five_ok,four_ok,full_house,three_ok,two_pair,pair,high_card]
for i in range(len(hand_lists)):
    hand_lists[i] = quickSort(hand_lists[i])

hand_lists.reverse()

sorted_hands = [inner
                    for outer in hand_lists
                        for inner in outer]

total_earnings = sum([int(sorted_hands[i][1])*(i+1) for i in range(len(sorted_hands))])
print(total_earnings)