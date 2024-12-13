import sys

directions = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

def read_map() -> tuple[list[list[bool]], int, int]:
    loc_x = 0
    loc_y = 0
    map = []
    with open(sys.argv[1]) as f:
        for y, line in enumerate(f):
            line = line.strip()
            map_row: list[bool] = []
            for x, spot in enumerate(line):
                if spot == '^':
                    loc_x = x
                    loc_y = y
                    map_row.append(True)
                elif spot == '.':
                    map_row.append(True)
                elif spot == '#':
                    map_row.append(False)
            map.append(map_row)

    return map, loc_x, loc_y

def inbounds(x: int, y: int, map: list[list[bool]]) -> bool:
    return y < len(map) and x < len(map[0])

def print_map(map: list[list[bool]]):
    for row in map:
        for spot in row:
            if spot:
                print('.', end='')
            else:
                print('#', end='')
        print()

def is_loop(map: list[list[bool]], x: int, y: int):
    spots: set[tuple[int, int, int]] = set()
    dir_index: int = 0

    try:
        while inbounds(x, y, map):
            if (x, y, dir_index) in spots:
                return True
            spots.add((x, y, dir_index))

            dx, dy = directions[dir_index]
            new_x = x + dx
            new_y = y + dy

            if new_x < 0 or new_y < 0:
                return False

            if map[new_y][new_x]:
                x = new_x
                y = new_y
            else:
                dir_index = (dir_index + 1) % len(directions)
    except IndexError:
        return False

def collect_spots(map: list[list[bool]], x: int, y: int) -> set[tuple[int, int]]:
    spots: set[tuple[int, int]] = set()
    dir_index: int = 0

    try:
        while inbounds(x, y, map):
            spots.add((x, y))

            new_x = x + directions[dir_index][0]
            new_y = y + directions[dir_index][1]

            if new_x < 0 or new_y < 0:
                break

            if map[new_y][new_x]:
                x = new_x
                y = new_y
            else:
                dir_index = (dir_index + 1) % 4
    except IndexError:
        pass

    return spots


def main():
    ways: set[tuple[int, int]] = set()
    map, x, y = read_map()

    spots = collect_spots(map, x, y)

    for (i, j) in spots:
        old = map[j][i]
        map[j][i] = False
        if is_loop(map, x, y):
            ways.add((i, j))

        map[j][i] = old

    print(len(ways))
            
main()
