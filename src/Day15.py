from queue import PriorityQueue


class Node:
    def __init__(self, value):
        self.value = int(value)-int(0)
        self.pre = None
        self.length = 10000
        self.x = 0
        self.y = 0

    def __repr__(self):
        return str(self.value) + '/' + str(self.length)

    def __lt__(self, other):
        return self.length < other.length

    def __le__(self, other):
        return self.length <= other.length


def parse_line(line):
    result = list(map(lambda c: Node(c), list(line)))
    return result


def visit(map, x, y, open_list):
    pass


def find_path(map, open_list):
    map[0][0].length = 0
    open_list.sort(reverse=True)
    while len(open_list) > 0:
        n = open_list.pop()
        if n.x == 9 and n.y == 9:
            print("finished ", n.length)
            return n
        nbs = []
        if n.x > 0:
            nbs.append(map[n.x-1][n.y])
        if n.x < 9:
            nbs.append(map[n.x+1][n.y])
        if n.y > 0:
            nbs.append(map[n.x][n.y-1])
        if n.y < 9:
            nbs.append(map[n.x][n.y+1])
        for nb in nbs:
            if nb in open_list:
                alt = n.length + nb.value
                if alt < nb.length:
                    nb.length = alt
                    nb.pre = n
                    open_list.sort(reverse=True)

#    visit(map, 0, 0, open_list)


def run(fname):
    fin = open(fname)
    map = []
    open_list = []
    y = 0
    for line in fin:
        if line.strip() != "":
            row = parse_line(line.strip())
            x = 0
            for n in row:
                open_list.append(n)
                n.x = x
                n.y = y
                x = x + 1
            y = y + 1
            map.append(row)

    goal = find_path(map, open_list)
    print(goal)
    n = goal
    while n is not None:
        print(n.x, n.y, n.value, n.length)
        n = n.pre
    print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run('../data/day15.txt')