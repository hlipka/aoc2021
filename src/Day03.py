length = 0
total = 0
counts = []


def parse(line):
    global length
    global counts
    for i in range(0, length):
        c = line[i]
        counts[i] = counts[i] + int(c)


def run(fname):
    global total
    global length
    global counts

    fin = open(fname)
    line = fin.readline()
    length = len(line)-1
    for i in range(0, length):
        counts.append(int(line[i]))

    for line in fin:
        total = total + 1
        if line != "":
            parse(line)

    half = total / 2
    gamma = '0b'
    epsilon = '0b'
    for i in range(0, length):
        if counts[i]>half:
            gamma = gamma + '1'
            epsilon = epsilon + '0'
        else:
            gamma = gamma + '0'
            epsilon = epsilon + '1'
    print(gamma)
    print(int(gamma, 0))
    print(epsilon)
    print(int(epsilon, 0))
    print(int(gamma, 0)*int(epsilon, 0))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run('../data/day03.txt')
