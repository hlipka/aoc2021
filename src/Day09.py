import numpy as np

def parse_line(line, amap):
    amap.append(list(map(lambda x: int(x), list(line))))


def is_low(sl):
    center = sl[1, 1]
    return center < sl[0, 0] and center < sl[0, 1] and center < sl[0, 2] and center < sl[1, 0] and center < sl[1, 2] and center < sl[2, 0] and center < sl[2, 1] and center < sl[2, 2]


def run(fname):
    amap = []
    fin = open(fname)
    for line in fin:
        if line.strip() != "":
            parse_line(line.strip(), amap)

    amap = np.asarray(amap)
    rows, cols = amap.shape
    amap = np.pad(amap, 1, mode='constant', constant_values=(10))
    # print(amap)
    score = 0
    for row in range(0, rows):
        for col in range(0, cols):
            sl = amap[row:row + 3, col:col + 3]
            # print(row, col, sl)
            if is_low(sl):
                # print('low')
                score = score + sl[1, 1] +1
    print(score)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run('../data/day09.txt')