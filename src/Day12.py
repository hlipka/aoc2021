
class Cave:
    def __init__(self, name):
        self.name = name
        self.targets = []
        self.big = name.isupper()
        self.start = (name == "start")
        self.end = (name == "end")

    def __repr__(self):
        return self.name

    def is_big(self):
        return self.big

    def is_start(self):
        return self.start

    def is_end(self):
        return self.end

    def add_target(self, cave):
        self.targets.append(cave)


def parse_line(line, caves):
    path = line.split('-')
    name1 = path[0]
    if name1 not in caves:
        cave1 = Cave(name1)
        caves[name1] = cave1
    else:
        cave1 = caves[name1]
    name2 = path[1]
    if name2 not in caves:
        cave2 = Cave(name2)
        caves[name2] = cave2
    else:
        cave2 = caves[name2]
    cave1.add_target(cave2)
    cave2.add_target(cave1)


def visit_paths(path, next, paths):
    if next.is_end():
        path.append(next)
        paths.append(path)
        return
    if next.is_big():
        path.append(next)
        for t in next.targets:
            visit_paths(list(path), t, paths)
    else:
        if next not in path:
            path.append(next)
            for t in next.targets:
                visit_paths(list(path), t, paths)


def run(fname):
    caves = {}
    fin = open(fname)
    for line in fin:
        if len(line.strip()) > 0:
            parse_line(line.strip(), caves)

    start = caves['start']
    paths = []

    path = []
    visit_paths(path, start, paths)

    print(paths)
    print(len(paths))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run('../data/day12.txt')