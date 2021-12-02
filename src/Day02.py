class Command:
    def __init__(self, direction, dist):
        if direction == 'forward':
            self.fwd = dist
            self.down = 0
        elif direction == 'down':
            self.fwd = 0
            self.down = dist
        elif direction == 'up':
            self.fwd = 0
            self.down = -dist


class Position:
    def __init__(self):
        self.h = 0
        self.d = 0

    def update(self, cmd):
        self.h = self.h + cmd.fwd
        self.d = self.d + cmd.down


def parse(line):
    parts = line.split(' ',1)
    return Command(parts[0], int(parts[1]))

def run(fname):
    fin = open(fname)
    pos = Position()
    for line in fin:
        if line != "":
            cmd = parse(line)
            pos.update(cmd)

    print(pos.h*pos.d)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run('../data/day02.txt')