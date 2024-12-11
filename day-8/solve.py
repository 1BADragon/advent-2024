import sys
from collections import defaultdict
from typing import DefaultDict

def main():
    locations: DefaultDict[str, list[tuple[int, int]]] = defaultdict(list)
    antinodes: DefaultDict[str, set[tuple[int, int]]] = defaultdict(set)
    antina_locs: set[tuple[int, int]] = set()
    width = 0
    height = 0
    q = 0

    map:list[list[str]] = list()

    with open(sys.argv[1]) as f:
        for j, line in enumerate(f):
            line = line.strip()
            width = len(line)
            height += 1
            for i, c in enumerate(line):
                if c != '.':
                    locations[c].append((i, j))
                    antina_locs.add((i, j))
                    q += 1
            map.append(list(line))

    for c in locations:
        l = locations[c]
        for l1 in l:
            for l2 in l:
                if l1 == l2:
                    continue
                dx = l1[0] - l2[0]
                dy = l1[1] - l2[1]

                ax = l1[0] + dx
                ay = l1[1] + dy

                if (ax, ay) not in antina_locs and 0 <= ax < width and 0 <= ay < height:
                    antinodes[c].add((ax, ay))
                    map[ay][ax] = '#'

                ax = l2[0] - dx
                ay = l2[1] - dy

                if (ax, ay) not in antina_locs and 0 <= ax < width and 0 <= ay < height:
                    antinodes[c].add((ax, ay))
                    map[ay][ax] = '#'

    print(sum(len(v) for v in antinodes.values()))

main()
