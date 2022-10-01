board = [[0] * 3 for n in range(3)]


def bestMove(board):
    best_move = float("-inf")
    for x in range(3):
        for y in range(3):
            if board[x][y] == 0:
                board[x][y] = 1
                score = minimax(board, 0, False)
                board[x][y] = 0
                if score > best_move:
                    best_move = score
                    moveX = x
                    moveY = y

    board[moveX][moveY] = 1


def minimax(board, turn, maximizing):
    result = check_won(board)
    if result != 0:
        if result == 1:
            return 10
        if result == -1:
            return -10
    if check_draw(board):
        return 0

    if maximizing:
        best_move = float("-inf")
        for x in range(3):
            for y in range(3):
                if board[x][y] == 0:
                    board[x][y] = 1
                    score = minimax(board, turn + 1, False)
                    board[x][y] = 0
                    best_move = max(score, best_move)

        return best_move
    else:
        best_move = float("inf")
        for x in range(3):
            for y in range(3):
                if board[x][y] == 0:
                    board[x][y] = -1
                    score = minimax(board, turn + 1, True)
                    board[x][y] = 0
                    best_move = min(score, best_move)

        return best_move


def check_draw(board):
    for x in range(3):
        for y in range(3):
            if board[x][y] == 0:
                return False
    return True


def check_won(board):
    won = False
    for x in range(3):
        local_value_row = board[x][0]
        local_value_col = board[0][x]
        if local_value_row != 0 and local_value_row == board[x][1]:
            if local_value_row == board[x][2]:
                return local_value_row
        if local_value_col != 0 and local_value_col == board[1][x]:
            if local_value_col == board[2][x]:
                return local_value_col

    if board[0][0] != 0 and board[0][0] == board[1][1]:
        if board[0][0] == board[2][2]:
            return board[0][0]
    if board[0][2] != 0 and board[0][2] == board[1][1]:
        if board[0][2] == board[2][0]:
            return board[0][2]
    return 0


def get_char(i):
    if i == 0:
        return " "
    if i == -1:
        return "O"
    if i == 1:
        return "X"


def draw_board(board):
    for x in range(3):
        print(
            f"{get_char(board[x][0])}|{get_char(board[x][1])}|{get_char(board[x][2])}"
        )
        if x != 2:
            print(f"-----")
    print("\n\n")


def ask_for_input(player):
    print("Where to go next? column,row")
    user_in = input()
    user_in = user_in.split(",")
    x = int(user_in[0])
    y = int(user_in[1])
    if board[x][y] != 0:
        return False
    board[x][y] = player
    return True


player = 0
while True:
    if player > 8:
        print("Draw!")
        break
    if (player % 2) == 1:
        while not ask_for_input(-1):
            print("Already Taken")
    else:
        bestMove(board)
    draw_board(board)
    won = check_won(board)
    if won != 0:
        print(f"{get_char(won)} Won!!!")
        break

    player = player + 1
