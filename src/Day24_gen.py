from math import trunc

input = 0


def parse(line):
    global input
    parts = line.split(' ')
    if parts[0] == 'inp':
        input += 1
        print("    return z\n\ndef step"+str(input)+"(w, z):")
    if parts[0] == 'add':
        print("   ", parts[1], "=", parts[1], "+", parts[2])
    if parts[0] == 'mul':
        if parts[2] == '0':
            print("   ", parts[1], "= 0")
        else:
            print("   ", parts[1], "=", parts[1], "*", parts[2])
    if parts[0] == 'div':
        print("   ", parts[1], "= trunc(", parts[1], "/", parts[2], ")")
    if parts[0] == 'mod':
        print("   ", parts[1], "=", parts[1], "%", parts[2])
    if parts[0] == 'eql':
        print("   ", parts[1], "= 1 if", parts[1], "==", parts[2], "else 0")


def run(f_name):
    fin = open(f_name)
    program = []

    for line in fin:
        line = line.strip()
        if line == '':
            continue
        parse(line)


if __name__ == '__main__':
    run('../data/day24.txt')
