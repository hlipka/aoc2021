def get_bits(c):
    if c == '0':
        return [0, 0, 0, 0]
    if c == '1':
        return [0, 0, 0, 1]
    if c == '2':
        return [0, 0, 1, 0]
    if c == '3':
        return [0, 0, 1, 1]
    if c == '4':
        return [0, 1, 0, 0]
    if c == '5':
        return [0, 1, 0, 1]
    if c == '6':
        return [0, 1, 1, 0]
    if c == '7':
        return [0, 1, 1, 1]
    if c == '8':
        return [1, 0, 0, 0]
    if c == '9':
        return [1, 0, 0, 1]
    if c == 'A':
        return [1, 0, 1, 0]
    if c == 'B':
        return [1, 0, 1, 1]
    if c == 'C':
        return [1, 1, 0, 0]
    if c == 'D':
        return [1, 1, 0, 1]
    if c == 'E':
        return [1, 1, 1, 0]
    if c == 'F':
        return [1, 1, 1, 1]
    return []

def parse_packet_line(line):
    print("parse", line)
    bits = []
    for c in line:
        bits.extend(get_bits(c))
    print(bits)
    parse_packet(bits)


def bits_to_number(bits):
    num = 0
    pos = 1
    for b in reversed(bits):
        num += b * pos
        pos *= 2
    return num


def parse_literal(bits):
    print("literal:", bits)
    p_count = 0
    result = []
    while bits[p_count * 5] == 1:
        packet = bits[p_count * 5 + 1:p_count * 5 + 5]
        print("cont", packet, bits_to_number(packet))
        result.extend(packet)
        p_count += 1
    packet = bits[p_count * 5 + 1:p_count * 5 + 5]
    print("last", packet, bits_to_number(packet))
    result.extend(packet)
    print("literal=", bits_to_number(result))
    return p_count * 5 + 5  # number of bits consumed


def parse_operator(bits):
    print("operator:", bits)
    if bits[0] == 1:
        length = bits_to_number(bits[1:12])
        print("sub-packet number", length)
        parsed_bits = 0
        parsed_packets = 0
        while parsed_packets < length:
            print("parse sub packet")
            pb = parse_packet(bits[parsed_bits + 12:])
            parsed_bits += pb
            parsed_packets += 1
        return parsed_bits + 12
    else:
        length = bits_to_number(bits[1:16])
        print("bit count", length)
        parsed_bits = 0
        while parsed_bits < length:
            print("parse sub packet")
            pb = parse_packet(bits[parsed_bits + 16:])
            parsed_bits += pb
        return length + 16

def parse_packet(bits):
    version = bits[:3]
    type = bits[3:6]
    print("v", version)
    print("t", type)
    if type == [1, 0, 0]:
        return parse_literal(bits[6:]) + 6
    else:
        return parse_operator(bits[6:]) + 6


def run(fname):
    fin = open(fname)
    line = fin.readline()
    parse_packet_line(line.strip())



#parse_packet_line("D2FE28")
#parse_packet_line("38006F45291200")
parse_packet_line("EE00D40C823060")

#if __name__ == '__main__':
#    run('../data/day16.txt')
