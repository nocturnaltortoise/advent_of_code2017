def take_step(maze, steps, i):
    old_maze_value = maze[i]
    maze[i] += 1
    i += old_maze_value
    steps += 1

    return maze, steps, i

with open('input.txt', 'r') as f:
    maze = [int(num) for num in f.readlines()]
    steps = 0
    i = 0

    maze, steps, i = take_step(maze, steps, i)
    while i < len(maze) and i >= 0:
        maze, steps, i = take_step(maze, steps, i)

    print(steps)
