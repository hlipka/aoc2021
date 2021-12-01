def run(fname):
    fin = open(fname)
    line = fin.readline()
    lastnum = int(line)
    increase = 0

    for line in fin:
        if line != "":
            num = int(line)
            if num > lastnum:
                increase = increase +1
            lastnum = num

    print(increase)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run('../data/day01.txt')