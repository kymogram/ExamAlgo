def superLabSolver(Plan, pos, I, B, path = []):
    if pos[0] == len(Plan[0]) and pos[1] == len(Plan):
        return Path
    else:
        if Plan[pos[0]][pos[1]] == 'I':
            I += 1
        elif Plan[pos[0]][pos[1]] == 'B':
            B += 1
        if move(Plan, pos, path, I, B) != "Wrong way":
            pos = move(Plan, pos, path, I, B)
        else:
            path.pop()
            # Je suis perdu

def move(Plan, pos, path, I, B):
    move = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    if I > 0:
        for i in range(len(move)):
            if checkWalls(Plan, pos, move, i) == 'x':
                # Si en le 'x' se trouve plus près de la fin que la position
                # actuelle, on utilise la super force
                if pos[0] - len(Plan[0]) < (pos[0] + move[i][0]) - len(Plan[0]) and \
                   pos[1] - len(plan) < pos[1] + move[i][1] - len(plan):
                    pos = (pos[0] + 2*(move[i][0]), pos[1] + 2*(move[i][1]), 'I')
                    path.append(pos)
                    return pos

    elif B > 0:
        for i in range(len(move)):
            tmp_pos = pos
            j = 0
            while checkWalls(Plan, tmp_pos, move, i) != 'x' and j < 3:
                tmp_pos = (pos[0]+move[i][0], pos[1]+move[i][1])
                j += 1
            if j == 3:
                pos = (pos[0] + 3*(move[i][0]), pos[1] + 3*(move[i][1]), 'B')
                path.append(pos)
                return pos

    for i in range(len(move)):
        if checkWalls(Plan, pos, move, i) == '':
            tmp_pos = (pos[0]+move[i][0], pos[1]+move[i][1])
            # On regarde si on n'est pas déjà passé par là
            if tmp_pos not in path:
                path.append(tmp_pos)
                return tmp_pos
            else:
                return "Wrong way"

def checkWalls(Plan, pos, move, i):
    # On vérifie que c'est bien dans le terrain
    if pos[0] + move[i][0] < len(Plan[0]) and \
       pos[1] + move[i][1] < len(Plan):
        return Plan[pos[0]+move[i][0]][pos[1]+move[i][1]]