with open('input.txt', 'r') as f:
    lines = f.readlines()

    checksum = 0
    for line in lines:
        line = [int(num) for num in line.split('\t')]
        found_division = False
        i = 0
        while not found_division and i < len(line):
            for j in range(i+1, len(line)):
                if line[i] == line[j]:
                    continue

                if line[i] % line[j] == 0:
                    even_divisors = (line[i], line[j])
                    found_division = True
                elif line[j] % line[i] == 0:
                    even_divisors = (line[j], line[i])
                    found_division = True
            i += 1

        print(even_divisors)
        checksum += (even_divisors[0] / even_divisors[1])

    print(checksum)
