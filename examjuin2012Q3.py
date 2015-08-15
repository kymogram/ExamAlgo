def findCheese(maze, maze_size, initial_pos):
    move = [[-1, 0], [0, -1], [+1, 0], [0, +1]]
    all_visited = False
    i = 1
    while not maze.success() or all_visited:
        if move(i):
            initial_pos[0] += move[i][0]
            initial_pos[1] += move[i][1]
        i += 1
        if i == 5:
            i = 1
    if all_visited and maze.success():
        print("Miam")
    else:
        print("Pourquoi tu me fais ça ?")