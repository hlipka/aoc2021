import re
import numpy as np

# pattern for a line
pattern = r'x=(\-?\d+)\.\.(\-?\d+),y=(\-?\d+)\.\.(\-?\d+),z=(\-?\d+)\.\.(\-?\d+)'


class Cube:
    def __init__(self, line):
        self.ofs = 50
        if line.startswith('on'):
            line = line[3:]
            self.value = 1
        else:
            line = line[4:]
            self.value = 0
        match = re.search(pattern, line)
        self.x_start = int(match.group(1))
        self.x_end = int(match.group(2))
        self.y_start = int(match.group(3))
        self.y_end = int(match.group(4))
        self.z_start = int(match.group(5))
        self.z_end = int(match.group(6))

    def fill_cube(self, amap, x_ofs, y_ofs, z_ofs):
        amap[
            self.x_start + x_ofs:self.x_end + x_ofs + 1,
            self.y_start + y_ofs:self.y_end + y_ofs + 1,
            self.z_start + z_ofs:self.z_end + z_ofs + 1] = self.value


def run(f_name):
    fin = open(f_name)

    cubes = []
    x_start = []
    x_end = []
    y_start = []
    y_end = []
    z_start = []
    z_end = []
    for line in fin:
        line = line.strip()
        if line == '':
            break
        cube = Cube(line)
        cubes.append(cube)
        x_start.append(cube.x_start)
        x_end.append(cube.x_end)
        y_start.append(cube.y_start)
        y_end.append(cube.y_end)
        z_start.append(cube.z_start)
        z_end.append(cube.z_end)

    x_ofs = - min(x_start)
    x_max = max(x_end)
    y_ofs = - min(z_start)
    y_max = max(z_end)
    z_ofs = - min(z_start)
    z_max = max(z_end)

    amap = np.zeros((x_ofs + x_max + 1, y_ofs + y_max + 1, z_ofs + z_max + 1), dtype=int)

    for cube in cubes:
        cube.fill_cube(amap, x_ofs, y_ofs, z_ofs)

    print(amap.shape)

    # create a new array which marks all places crossed more than once
    mark = amap.flat == 1
    # select these elements, and sum them up
    crosses = amap.flat[mark]
    print(sum(crosses))


if __name__ == '__main__':
    run('../data/day22.txt')
