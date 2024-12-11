import sys

directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

def read_map() -> list[list[int]]:
    map: list[list[int]] = []
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip()
            map.append([int(x) for x in line])

    return map

# scores: dict[tuple[int, int], int] = {}
def score_at(map: list[list[int]], x: int, y: int, nines: set[tuple[int, int]]) -> int:
    # if (x, y) in scores:
    #     return 0
        # return scores[(x, y)]

    if y < 0 or y >= len(map):
        return 0

    if x < 0 or x >= len(map[y]):
        return 0

    curr = map[y][x]
    print(x, y, curr)
    if curr == 9:
        if (x, y) in nines:
            return 0
        nines.add((x, y))
        return 1

    score = 0
    for dx, dy in directions:
        x2 = x + dx
        y2 = y + dy
        if y2 < 0 or y2 >= len(map) or x2 < 0 or x2 >= len(map[y2]):
            continue
        next = map[y2][x2]
        if next == curr + 1:
            score += score_at(map, x2, y2, nines)

    # scores[(x, y)] = score
    return score
    

def main():
    map = read_map()

    map_score = 0

    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 0:
                map_score += score_at(map, x, y, set())

    print(map_score)

main()
