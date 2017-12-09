with open('input.txt', 'r') as f:
    lines = f.readlines()
    checksum = 0
    for line in lines:
        line = [int(num) for num in line.split('\t')]
        line_range = max(line) - min(line)
        print(line_range)
        checksum += line_range

    print(checksum)
