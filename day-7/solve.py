import sys

def has_solution(solution, factors, curr_value):
    if not factors:
        return solution == curr_value

    return (
        has_solution(solution, factors[1:], curr_value + factors[0]) or
        has_solution(solution, factors[1:], curr_value * factors[0]) or
        has_solution(solution, factors[1:], int(str(curr_value) + str(factors[0])))
    )

def main():
    with open(sys.argv[1]) as f:
        sum = 0
        for line in f:
            left, right = line.split(':')
            solution = int(left)
            factors = [int(v) for v in right.strip().split(' ')]

            if has_solution(solution, factors[1:], factors[0]):
               sum += solution 

    print(sum)

main()
