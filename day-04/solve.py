directions = [
    (((-1, -1), (-1, 1)), ((1, -1), (1, 1))),
    (((1, -1), (1, 1)), ((-1, -1), (-1, 1))),
    (((1, -1), (-1, -1)), ((1, 1), (-1, 1))),
    (((1, 1), (-1, 1)), ((1, -1), (-1, -1))),
]

used: set[tuple[int, int]] = set()

def search(
    map: list[list[str]], 
    loc: tuple[int, int], 
    direction: tuple[
        tuple[tuple[int, int], tuple[int, int]], 
        tuple[tuple[int, int], tuple[int, int]]
    ]
) -> bool:
    x, y = loc
    points = []

    if x <= 0 or y <= 0:
        return False

    points.append((x, y))
    if map[y][x] != 'A':
        return False

    for dx, dy in direction[0]:
        points.append((x+dx, y+dy))
        if map[y+dy][x+dx] != 'M':
            return False

    for dx, dy in direction[1]:
        points.append((x+dx, y+dy))
        if map[y+dy][x+dx] != 'S':
            break
    else:
        used.update(points)
        return True

    return False

def main():
    map = []
    count = 0

    with open('input') as f:
        for line in f:
            map.append(list(line.strip()))

    for y in range(len(map)):
        for x in range(len(map[y])):
            for d in directions:
                try:
                    if search(map, (x, y), d):
                        count += 1
                except IndexError:
                    pass

    for y in range(len(map)):
        for x in range(len(map[y])):
            if (x, y) in used:
                print(map[y][x], end='')
            else:
                print('.', end='')
        print()

    print(count)

main()
