transformations = [
    # x is facing x
    lambda x, y, z: [x, y, z],
    lambda x, y, z: [x, -z, y],
    lambda x, y, z: [x, -y, -z],
    lambda x, y, z: [x, z, -y],
    # x is facing -x
    lambda x, y, z: [-x, -y, z],
    lambda x, y, z: [-x, -z, -y],
    lambda x, y, z: [-x, y, -z],
    lambda x, y, z: [-x, z, y],
    # x is facing y
    lambda x, y, z: [-z, x, -y],
    lambda x, y, z: [y, x, -z],
    lambda x, y, z: [z, x, y],
    lambda x, y, z: [-y, x, z],
    # x is facing -y
    lambda x, y, z: [z, -x, -y],
    lambda x, y, z: [y, -x, z],
    lambda x, y, z: [-z, -x, y],
    lambda x, y, z: [-y, -x, -z],
    # x is facing z
    lambda x, y, z: [-y, -z, x],
    lambda x, y, z: [z, -y, x],
    lambda x, y, z: [y, z, x],
    lambda x, y, z: [-z, y, x],
    # x is facing -z
    lambda x, y, z: [z, y, -x],
    lambda x, y, z: [-y, z, -x],
    lambda x, y, z: [-z, -y, -x],
    lambda x, y, z: [y, -z, -x]
]


class Scanner:
    def __init__(self):
        self.beacons = []
        self.transformed_beacons = []

    def add_beacon(self, beacon):
        self.beacons.append(beacon)

    def prepare(self):
        pass  # FIXME implement - calculate distances between all beacons and store them


class Beacon:
    def __init__(self, coords):
        self.coords = coords
        self.transformed_coords = coords


def parse_coord(line):
    coords = line.split(',')
    return Beacon((coords[0], coords[1], coords[2]))


def run(fname):
    scanners = []
    scanner = None
    fin = open(fname)
    for line in fin:
        line = line.strip()
        if line != '':
            if line.startswith('--- scanner'):
                scanner = Scanner()
                scanners.append(scanner)
            else:
                scanner.add_beacon(parse_coord(line))
    for scanner in scanners:
        scanner.prepare()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run('../data/day19.txt')
