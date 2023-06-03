n = int(input())
pairs = []
pair_outcome=[]
for _ in range(n):
    i, p = map(int, input().split())
    pairs.append((i, p))

for l in pairs:
    pair_outcome.append(l[1]-l[0])



# n =number of rooms
# i =number of people who already live in the room
# p =room capacity

place=0
georgeandfriend=2

for x in pair_outcome:
    if x>=georgeandfriend:
        place+=1


print(place)
    