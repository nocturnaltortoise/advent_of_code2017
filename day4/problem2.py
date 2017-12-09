with open('input.txt', 'r') as f:
    valid_count = 0
    for line in f:
        words = line.strip().split(' ')
        # problem 2
        words = ["".join(sorted(word)) for word in words]
        unique_words = set(words)

        if len(words) == len(unique_words):
            valid_count += 1

        print(words, unique_words, valid_count)

print(valid_count)
