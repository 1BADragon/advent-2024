import sys

def read_disk():
    fileno = 0
    disk: list[int | None] = []
    file_sizes: dict[int, tuple[int, int]] = {}
    with open(sys.argv[1]) as f:
        s = f.read().strip()            

    for i in range(0, len(s), 2):
        file_sizes[fileno] = (int(s[i]), len(disk))
        disk.extend([fileno] * int(s[i]))
        fileno += 1
        try:
            disk.extend([None] * int(s[i+1]))
        except IndexError:
            break
    return disk, fileno, file_sizes

def main():
    disk, max_fileno, file_sizes = read_disk()

    i = 0
    j = len(disk) - 1

    for place, fileno in enumerate(reversed(range(max_fileno))):
        if place % 1000 == 0:
            print(f'\r{round(((place+1) / max_fileno) * 100, 2)}', end='')

        size, offset = file_sizes[fileno]

        for i in range(offset):
            if disk[i] is None:
                free_space = 0
                j = i
                while j < len(disk) and disk[j] is None:
                    free_space += 1
                    j += 1
                if free_space >= size:
                    for j in range(size):
                        disk[i + j] = fileno
                        disk[offset + j] = None
                    file_sizes.pop(fileno)
                    i+= size
                    break
    print()
                    
    checksum = 0
    for i in range(len(disk)):
        fileno = disk[i]
        if fileno is not None:
            checksum += fileno * i

    print(checksum)

main()
