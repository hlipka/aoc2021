def parse_char(c, stack):
    if c == '(':
        stack.append(c)
    if c == '[':
        stack.append(c)
    if c == '{':
        stack.append(c)
    if c == '<':
        stack.append(c)
    if c == ')':
        c1 = stack.pop()
        return c1 == '('
    if c == ']':
        c1 = stack.pop()
        return c1 == '['
    if c == '}':
        c1 = stack.pop()
        return c1 == '{'
    if c == '>':
        c1 = stack.pop()
        return c1 == '<'


def parse_line(line):
    stack = []
    for c in line:
        if not parse_char(c, stack):
            if c == ')': return 3
            if c == ']': return 57
            if c == '}': return 1197
            if c == '>': return 25137
    return 0


def run(fname):
    score = 0
    fin = open(fname)
    for line in fin:
        if line.strip() != "":
            score = score + parse_line(line.strip())

    print(score)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run('../data/day10.txt')