import sys


def parse_line(line):
    left, right = line.split('->')
    left = left.split('+')
    right = right.split('+')
    return set(left), set(right)


def main():
    initial_elements = sys.stdin.readline().split()
    lefts = dict()
    rights = dict()
    for index, line in enumerate(sys.stdin):
        line = line.strip()
        if '->' not in line:
            break
        left, right = parse_line(line)
        lefts[index] = left
        rights[index] = right

    total_elements = set(initial_elements)
    proceed = True
    while proceed:
        good_keys = list()
        for key, value in lefts.items():
            if value <= total_elements:
                total_elements |= rights[key]
                good_keys.append(key)
        if len(good_keys) == 0:
            proceed = False
        else:
            for key in good_keys:
                del lefts[key]
    print(' '.join(total_elements))


if __name__ == '__main__':
    main()
