class Data:
    def __init__(self, line):
        data = line.split('|')
        self.in_patterns = data[0].strip().split(' ')
        self.display_patterns = data[1].strip().split(' ')

def run(fname):
    fin = open(fname)
    data = []
    count = 0
    for line in fin:
        data.append(Data(line.strip()))
    for dat in data:
        for dp in dat.display_patterns:
            l = len(dp)
            if l == 2 or l == 3 or l == 4 or l == 7:
                count = count + 1
    print(count)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run('../data/day08.txt')