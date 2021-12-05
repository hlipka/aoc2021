import numpy as np


class Board:
    def __init__(self, lines):
        ml = ' '.join(lines).replace('\n','')
        self.data = np.fromstring(ml, sep=' ')
        self.data = self.data.reshape(5, 5)

    def cross(self, num):
        self.data[self.data == num]=-1

    def row_selected(self, row):
        return (row == -1).all()

    def is_winner(self):
        for row in self.data:
            if self.row_selected(row):
                return True
        for row in self.data.transpose():
            if self.row_selected(row):
                return True

    def get_unselected(self):
        get = self.data.flat != -1
        return self.data.flat[get]



def run(fname):
    boards = []
    lastscore = 0
    fin = open(fname)
    line = fin.readline()
    nums = line.replace('\n','').split(',')
    fin.readline()
    boardlines=[]
    for l in fin:
        if l == '\n':
            boards.append(Board(boardlines))
            boardlines = []
        else:
            boardlines.append(l)
    for num in nums:
        print("cross "+num)
        removed=[]
        for board in boards:
            board.cross(int(num))
            if num=='13':
                print(board.data)
            if board.is_winner():
                us = board.get_unselected()
                s = sum(us)
                lastscore = int(num)*s
                removed.append(board)
                print(board.data)
        for b in removed:
            boards.remove(b)
        if 0 == len(boards):
            print("done")
            break
    print(lastscore)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run('../data/day04.txt')