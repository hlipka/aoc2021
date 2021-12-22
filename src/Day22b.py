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

        # TODO sort coordinates so the regions are oriented properly

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

    def overlaps_any(self, regions):
        for r in regions:
            if r is not self:
                if self.overlaps(r):
                    return True
        return False

    # FIXME I don't think this check is correct
    # there is no overlap if for any axis there is no overlap
    def overlaps(self, region):
        if self.contains(region.x_start, region.y_start, region.z_start) or \
           self.contains(region.x_start, region.y_start, region.z_end) or \
           self.contains(region.x_start, region.y_end, region.z_start) or \
           self.contains(region.x_start, region.y_end, region.z_end) or \
           self.contains(region.x_end, region.y_start, region.z_start) or \
           self.contains(region.x_end, region.y_start, region.z_end) or \
           self.contains(region.x_end, region.y_end, region.z_start) or \
           self.contains(region.x_end, region.y_end, region.z_end):
            return True
        return False

    def contains(self, x, y, z):
        return self.x_start <= x < self.x_end and self.y_start <= y < self.y_end and self.z_start <= z < self.z_end


def run(f_name):
    fin = open(f_name)

    cubes = []
    for line in fin:
        line = line.strip()
        if line == '':
            break
        cube = Cube(line)
        cubes.append(cube)

    # discard any regions which are contained fully in a later region
    # (they will not do anything)

    # single out all region which do not overlap anything else, and are not contained in an earlier region
    # keep the 'on' regions, and discard the 'off' regions (they do not do anything)

    # go through all regions in order
    #   for any overlap with an existing region, store a new overlap region with the opposing sign
    #   if its an 'on' region, store it

    # when all steps are finished, run through all regions and count their cubes

    # result for demo data: 2758514936282235


if __name__ == '__main__':
    run('../data/day22.txt')
