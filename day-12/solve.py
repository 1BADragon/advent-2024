import sys

directions = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

def read_map() -> list[list[str]]:
    map: list[list[str]] = []
    with open(sys.argv[1]) as f:
        for line in f:
            map.append(list(line.strip()))
    return map

def collect_region(map: list[list[str]], x: int, y: int) -> set[tuple[int, int]]:
    region: set[tuple[int, int]] = set()
    
    c = map[y][x]
    stack = [(x, y)]
    while stack:
        x1, y1 = stack.pop()

        if y1 < 0 or y1 >= len(map) or x1 < 0 or x1 >= len(map[y1]):
            continue
        
        s = map[y1][x1]

        if c != s or (x1, y1) in region:
            continue

        for dx, dy in directions:       
            x2 = x1 + dx
            y2 = y1 + dy
            stack.append((x2, y2))

        region.add((x1, y1))

    return region
        
def score(map: list[list[str]], x: int, y: int) -> int:
    p = 4

    for dx, dy in directions:
        x1 = x + dx
        y1 = y + dy

        if y1 < 0 or y1 >= len(map) or x1 < 0 or x1 >= len(map[y1]):
            continue

        if map[y1][x1] == map[y][x]:
            p -= 1

    return p

def region_bounds(points: set[tuple[int, int]]) -> tuple[tuple[int, int], tuple[int, int]]:
    xmin = 100000000
    ymin = 100000000
    xmax = 0
    ymax = 0

    for x, y in points:
        if x < xmin:
            xmin = x
        if y < ymin:
            ymin = y

        if x > xmax:
            xmax = x
        if y > ymax:
            ymax = y

    return (xmin, ymin), (xmax, ymax)


def count_region_sides(map, points: set[tuple[int, int]], c) -> int:
    sides = 0
    (xmin, ymin), (xmax, ymax) = region_bounds(points)

    # horizontal run
    for y in range(ymin, ymax+2):
        on_edge = False
        edge_up = False
        for x in range(xmin, xmax+1):
            s = None
            if y < len(map) and (x, y) in points:
                s = map[y][x]

            up = None
            if y > 0 and (x, y-1) in points:
                up = map[y-1][x]

            if s == up:
                on_edge = False
            elif on_edge:
                if s != c and up != c:
                    on_edge = False
                elif s == c and edge_up:
                    edge_up = False
                    sides += 1
                elif up == c and not edge_up:
                    edge_up = True
                    sides += 1
            else:
                if s == c:
                    sides += 1
                    on_edge = True
                    edge_up = False
                elif up == c:
                    sides += 1
                    on_edge = True
                    edge_up = True

    # vertical run
    for x in range(xmin, xmax + 2):
        on_edge = False
        edge_left = False
        for y in range(ymin, ymax + 1):
            s = None
            if x < len(map[y]) and (x, y) in points:
                s = map[y][x]

            left = None
            if x > 0 and (x-1, y) in points:
                left = map[y][x-1]

            if s == left:
                on_edge = False
            elif on_edge:
                if s != c and left != c:
                    on_edge = False
                elif s == c and edge_left:
                    edge_left = False
                    sides += 1
                elif left == c and not edge_left:
                    edge_left = True
                    sides += 1
            else:
                if s == c:
                    sides += 1
                    on_edge = True
                    edge_left = False
                elif left == c:
                    sides += 1
                    on_edge = True
                    edge_left = True
    
    return sides

def main():
    map: list[list[str]] = read_map()

    sum1 = 0
    sum2 = 0
    calculated_spots: set[tuple[int, int]] = set()
    for j in range(len(map)):
        for i in range(len(map[j])):
            if (i, j) in calculated_spots:
                continue
            c = map[j][i]
            region = collect_region(map, i, j)

            area = len(region)
            perm = 0
            for x, y in region:
                perm += score(map, x, y)

            nsides = count_region_sides(map, region, c)
            sum1 += area * perm
            sum2 += area * nsides

            calculated_spots.update(region)

            # print(c, area, perm, area * perm)
            # print(c, area, nsides, area * nsides)

    # print(sum1)
    print(sum2)

main()
