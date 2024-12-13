import sys


def get_stones():
    with open(sys.argv[1]) as f:
        return [int(x) for x in f.read().strip().split(" ")]


def transform_stone(stone: int) -> list[int]:
    if stone == 0:
        return [1]

    d = str(stone)
    l = len(d)  # noqa: E741
    if l % 2 == 0:
        return [int(d[: l // 2]), int(d[l // 2 :])]

    return [stone * 2024]


def blink(stones: list[int]) -> list[int]:
    ret = []

    for stone in stones:
        ret.extend(transform_stone(stone))

    return ret


def main():
    stones = get_stones()

    for i in range(75):
        print(f"\r{i} -- {len(stones)}", end="")
        stones = blink(stones)

    print()

    print(len(stones))


main()
