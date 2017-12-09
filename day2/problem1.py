with open('input.txt', 'r') as f:
    checksum = 0
    for line in f:
        line = [int(num) for num in line.split('\t')]
        line_range = max(line) - min(line)
        print(line_range)
        checksum += line_range

    print(checksum)
