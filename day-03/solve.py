import re

r = re.compile(r"(?:mul\((\d{1,3}),(\d{1,3})\))|(?:do\(\))|(?:don't\(\))")

sum = 0
enabled = True

with open('input') as f:
    for match in r.finditer(f.read()):
        if match[0] == 'do()':
            enabled = True
        elif match[0] == "don't()":
            enabled = False
        elif enabled:
            sum += int(match[1]) *  int(match[2])

print(sum)
        
