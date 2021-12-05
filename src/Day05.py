import re
import numpy as np

pattern = r'(\d+),(\d+) -> (\d+),(\d+)'


class Line:
    def __init__(self, line):
        match = re.search(pattern, line)
        self.x_start = int(match.group(1))
        self.y_start = int(match.group(2))
        self.x_end = int(match.group(3))
        self.y_end = int(match.group(4))

    def dump(self):
        print(self.x_start, self.y_start, self.x_end, self.y_end)

    def max_x(self):
        return max(self.x_start, self.x_end)

    def max_y(self):
        return max(self.y_start, self.y_end)

    def draw_line_x(self, amap):
        for i in range(self.y_start, self.y_end):
            amap[self.x_start][i] = amap[self.x_start][i] + 1

    def draw_line_y(self, amap):
        for i in range(self.x_start, self.x_end):
            amap[i][self.y_start] = amap[i][self.y_start] + 1

    def draw_line(self, amap):
        if self.x_start == self.x_end:
            self.draw_line_y(amap)
        elif self.y_start == self.y_end:
            self.draw_line_y(amap)
        return

def run(fname):
    fin = open(fname)
    lines = []
    amap = np.full((10, 10), 0)

    for line in fin:
        line = line.strip()
        if line == '':
            break
        l = Line(line)
        l.dump()
        l.draw_line(amap)
        print(amap)

    mark = amap.flat > 1
    crosses = amap.flat[mark]
    print(len(crosses))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run('../data/day05.txt')