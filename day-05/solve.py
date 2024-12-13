import sys
import re
import itertools
from collections import defaultdict

rule_re = re.compile(r'(\d+)\|(\d+)')

def is_valid(update: list[int], rules: dict[int, set[int]]) -> bool:
    positions = {n: i for i, n in enumerate(update)}

    for before, afters in rules.items():
        if before not in positions:
            continue

        before_loc = positions[before]

        for a in afters:
            if a in positions:
                if before_loc > positions[a]:
                    return False

    return True

def fix(update: list[int], rules: dict[int, set[int]]) -> list[int]:
    positions = {n: i for i, n in enumerate(update)}

    while not is_valid(sorted(update, key=lambda x: positions[x]), rules):
        for before, afters in rules.items():
            if before not in positions:
                continue

            before_loc = positions[before]

            for after in afters:
                if after not in positions:
                    continue

                loc = positions[after]

                if before_loc >= loc:
                    positions[after] = before_loc + 1

    return sorted(update, key=lambda x: positions[x])

def main():
    rules: dict[int, set[int]] = defaultdict(set)
    updates: list[list[int]] = list()

    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip()

            if not line:
                break

            m = rule_re.match(line)
            assert m
            rules[int(m[1])].add(int(m[2]))

        for line in f:
            updates.append([int(x) for x in line.strip().split(',')])

    good_sum = 0
    fixed_sum = 0
    for update in updates:
        if is_valid(update, rules):
            good_sum += update[len(update) // 2]
        else:
            fixed = fix(update, rules)
            fixed_sum += fixed[len(update) // 2]

    print(good_sum)
    print(fixed_sum)
      
main()
