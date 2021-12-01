class SlidingWindow(object):
    def __init__(self, fname):
        self.fin = open(fname)
        v1 = int (self.fin.readline())
        v2 = int (self.fin.readline())
        self.buf = [0, v1, v2]

    def next_value(self):
        line = self.fin.readline()
        if line == "":
            return -1
        val = int(line)
        del(self.buf[0])
        self.buf.append(val)
        return sum(self.buf)


def run(fname):
    w = SlidingWindow(fname)
    lastnum = w.next_value()
    num = 0
    increase = 0
    while num != -1:
        num = w.next_value()
        if num > lastnum:
            increase = increase +1
        lastnum = num

    print(increase)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run('../data/day01.txt')