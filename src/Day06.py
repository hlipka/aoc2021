def run(fname):
    fin = open(fname)
    fish_line = fin.readline().strip()
    fishes = list(map(lambda f: int(f), fish_line.split(',')))

    for day in range(0, 80):
        for i in range(0, len(fishes)):
            if 0 == fishes[i]:
                fishes[i] = 6
                fishes.append(8)
            else:
                fishes[i] = fishes[i] -1


    print(len(fishes))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run('../data/day06.txt')