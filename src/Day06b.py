import numpy as np

def run(fname):
    fin = open(fname)
    fish_line = fin.readline().strip()
    fish_data = fish_line.split(',')
    fishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for fd in fish_data:
        days = int(fd)
        fishes[days] = fishes[days] + 1

    print(fishes)

    for day in range(0, 256):
        print(day, sum(fishes))
        new_fish = fishes[0]
        for i in range(0, 8):
            fishes[i] = fishes[i+1]
        fishes[8] = new_fish
        fishes[6] = fishes[6] + new_fish

    print(sum(fishes))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run('../data/day06.txt')