def move_crabs(crabs, pos):
    fuel = 0
    for crab in crabs:
        n = abs(crab - pos)
        fuel = fuel + (n * (n + 1) / 2)
    return fuel


def run(fname):
    fin = open(fname)
    crab_line = fin.readline().strip()
    crabs = list(map(lambda f: int(f), crab_line.split(',')))
    print(crabs)
    min_pos = min(crabs)
    max_pos = max(crabs)
    min_fuel = move_crabs(crabs, max_pos)

    for pos in range(min_pos, max_pos):
        fuel = move_crabs(crabs, pos)
        if fuel < min_fuel:
            print(pos)
            min_fuel = fuel

    print(min_fuel)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run('../data/day07.txt')