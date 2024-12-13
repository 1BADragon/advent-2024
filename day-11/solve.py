import sys
import functools


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


@functools.lru_cache(100000)
def blink(stone: int, remaining: int) -> int:
    if remaining == 0:
        return 0

    t = transform_stone(stone)
    sum = 0
    if remaining == 1:
        sum = len(t)
    for s in t:
        sum += blink(s, remaining - 1)

    return sum


def main():
    stones = get_stones()

    sum = 0
    for stone in stones:
        sum += blink(stone, 75)

    print(sum)


main()
