from collections import defaultdict

left = []
right = []
with open('input') as f:
    for line in f:
        split = line.split()
        left.append(int(split[0]))
        right.append(int(split[1]))

left.sort()
right.sort()

diff = 0
for l,r in zip(left, right):
    diff += abs(l - r)

print(diff)

counts = defaultdict(lambda : 0)
for r in right:
    counts[r] += 1

likeness = 0
for l in left:
    likeness += l * counts[l]

print(likeness)
