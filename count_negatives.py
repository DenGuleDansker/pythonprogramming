def negatives_of(lines):
    count = 0
    i = 0
    while i < len(lines):
        if float(lines[i]) < 0:
            count = count + 1
        i = i + 1
    return count

if __name__ == '__main__':
    import sys
    with open(sys.argv[1]) as file:
        lines = file.readlines()
        print(negatives_of(lines))