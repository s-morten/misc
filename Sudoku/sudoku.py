import keyboard
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM
import time
import _thread

BOARDLENGTH = 9
MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board
#
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

# board = [
#     [3, 4, 0, 8, 2, 6, 0, 7, 1],
#     [0, 0, 8, 0, 0, 0, 9, 0, 0],
#     [7, 6, 0, 0, 9, 0, 0, 4, 3],
#     [0, 8, 0, 1, 0, 2, 0, 3, 0],
#     [0, 3, 0, 0, 0, 0, 0, 9, 0],
#     [0, 7, 0, 9, 0, 4, 0, 1, 0],
#     [8, 2, 0, 0, 4, 0, 0, 5, 9],
#     [0, 0, 7, 0, 0, 0, 3, 0, 0],
#     [4, 1, 0, 3, 8, 9, 0, 6, 2],
# ]
given = [[False] * 9 for n in range(9)]


class SudokuGUI(Frame):
    def __init__(self, parent, game):
        self.game = game
        self.parent = parent
        Frame.__init__(self, parent)

        self.row, self.col = 0, 0

        self.__initUI()

    def __initUI(self):
        self.parent.title("Sudoku")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self, width=WIDTH, height=HEIGHT)
        self.canvas.pack(fill=BOTH, side=TOP)
        solve_button = Button(self, text="Solve", command=self.__solve)
        solve_button.pack(fill=BOTH, side=BOTTOM)

        self.__draw_grid()
        self.__draw_puzzle()
        self.updater()

        # self.canvas.bind("<Button-1>", self.__cell_clicked)
        # self.canvas.bind("<Key>", self.__key_pressed)

    def __draw_grid(self):
        """
        Draws grid divided with blue lines into 3x3 squares
        """
        for i in range(10):
            color = "blue" if i % 3 == 0 else "gray"

            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = MARGIN
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN
            y1 = MARGIN + i * SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

    def __draw_puzzle(self):
        self.canvas.delete("numbers")
        for i in range(9):
            for j in range(9):
                answer = self.game[i][j]
                if answer != 0:
                    x = MARGIN + j * SIDE + SIDE / 2
                    y = MARGIN + i * SIDE + SIDE / 2
                    # original = self.game.start_puzzle[i][j]
                    # color = "black" if answer == original else "sea green"
                    self.canvas.create_text(
                        # x, y, text=answer, tags="numbers", fill=color
                        x,
                        y,
                        text=answer,
                        tags=f"numbers{x}{y}",
                        fill="green",
                    )

    def __solve(self):
        _thread.start_new_thread(SudokuGame.solve, (0, 0))
        print("Startet Thread")

    def update_puzzle(self):
        for i in range(9):
            for j in range(9):
                answer = board[i][j]
                if answer != 0:
                    x = MARGIN + j * SIDE + SIDE / 2
                    y = MARGIN + i * SIDE + SIDE / 2
                    # original = self.game.start_puzzle[i][j]
                    # color = "black" if answer == original else "sea green"
                    if not given[i][j]:
                        self.canvas.delete(f"numbers{x}{y}")
                        self.canvas.create_text(
                            # x, y, text=answer, tags="numbers", fill=color
                            x,
                            y,
                            text=answer,
                            tags=f"numbers{x}{y}",
                            fill="black",
                        )

    def updater(self):
        self.update_puzzle()
        self.after(1, self.updater)


class SudokuGame:
    def printBoard():
        for x in range(0, 9):
            for y in range(0, 9):
                print(board[x][y], end=" ")
            print("\n")

    def checkRules(a, b):
        iAm = board[a][b]
        count = 0
        for x in range(0, 9):
            if board[x][b] == iAm:
                count = count + 1
                if count >= 2:
                    # print("error!")
                    return False

        count = 0
        for y in range(0, 9):
            if board[a][y] == iAm:
                count = count + 1
                if count >= 2:
                    # print("error!")
                    return False

        if a == 0 or a == 3 or a == 6:
            if b == 0 or b == 3 or b == 6:
                if board[a + 1][b] == iAm or board[a + 2][b] == iAm:
                    return False
                if (
                    board[a + 1][b + 1] == iAm
                    or board[a + 2][b + 1] == iAm
                    or board[a][b + 1] == iAm
                ):
                    return False
                if (
                    board[a + 1][b + 2] == iAm
                    or board[a + 2][b + 2] == iAm
                    or board[a][b + 2] == iAm
                ):
                    return False
            if b == 1 or b == 4 or b == 7:
                if board[a + 1][b] == iAm or board[a + 2][b] == iAm:
                    return False
                if (
                    board[a + 1][b - 1] == iAm
                    or board[a + 2][b - 1] == iAm
                    or board[a][b - 1] == iAm
                ):
                    return False
                if (
                    board[a + 1][b + 1] == iAm
                    or board[a + 2][b + 1] == iAm
                    or board[a][b + 1] == iAm
                ):
                    return False
            if b == 2 or b == 5 or b == 8:
                if board[a + 1][b] == iAm or board[a + 2][b] == iAm:
                    return False
                if (
                    board[a + 1][b - 2] == iAm
                    or board[a + 2][b - 2] == iAm
                    or board[a][b - 2] == iAm
                ):
                    return False
                if (
                    board[a + 1][b - 1] == iAm
                    or board[a + 2][b - 1] == iAm
                    or board[a][b - 1] == iAm
                ):
                    return False
        if a == 1 or a == 4 or a == 7:
            if b == 0 or b == 3 or b == 6:
                if board[a + 1][b] == iAm or board[a - 1][b] == iAm:
                    return False
                if (
                    board[a + 1][b + 1] == iAm
                    or board[a - 1][b + 1] == iAm
                    or board[a][b + 1] == iAm
                ):
                    return False
                if (
                    board[a + 1][b + 2] == iAm
                    or board[a - 1][b + 2] == iAm
                    or board[a][b + 2] == iAm
                ):
                    return False
            if b == 1 or b == 4 or b == 7:
                if board[a + 1][b] == iAm or board[a - 1][b] == iAm:
                    return False
                if (
                    board[a + 1][b - 1] == iAm
                    or board[a - 1][b - 1] == iAm
                    or board[a][b - 1] == iAm
                ):
                    return False
                if (
                    board[a + 1][b + 1] == iAm
                    or board[a - 1][b + 1] == iAm
                    or board[a][b + 1] == iAm
                ):
                    return False
            if b == 2 or b == 5 or b == 8:
                if board[a + 1][b] == iAm or board[a - 1][b] == iAm:
                    return False
                if (
                    board[a + 1][b - 2] == iAm
                    or board[a - 1][b - 2] == iAm
                    or board[a][b - 2] == iAm
                ):
                    return False
                if (
                    board[a + 1][b - 1] == iAm
                    or board[a - 1][b - 1] == iAm
                    or board[a][b - 1] == iAm
                ):
                    return False
        if a == 2 or a == 5 or a == 8:
            if b == 0 or b == 3 or b == 6:
                if board[a - 1][b] == iAm or board[a - 2][b] == iAm:
                    return False
                if (
                    board[a - 1][b + 1] == iAm
                    or board[a - 2][b + 1] == iAm
                    or board[a][b + 1] == iAm
                ):
                    return False
                if (
                    board[a - 1][b + 2] == iAm
                    or board[a - 2][b + 2] == iAm
                    or board[a][b + 2] == iAm
                ):
                    return False
            if b == 1 or b == 4 or b == 7:
                if board[a - 1][b] == iAm or board[a - 2][b] == iAm:
                    return False
                if (
                    board[a - 1][b - 1] == iAm
                    or board[a - 2][b - 1] == iAm
                    or board[a][b - 1] == iAm
                ):
                    return False
                if (
                    board[a - 1][b + 1] == iAm
                    or board[a - 2][b + 1] == iAm
                    or board[a][b + 1] == iAm
                ):
                    return False
            if b == 2 or b == 5 or b == 8:
                if board[a - 2][b] == iAm or board[a - 1][b] == iAm:
                    return False
                if (
                    board[a - 2][b - 2] == iAm
                    or board[a - 1][b - 2] == iAm
                    or board[a][b - 2] == iAm
                ):
                    return False
                if (
                    board[a - 2][b - 1] == iAm
                    or board[a - 1][b - 1] == iAm
                    or board[a][b - 1] == iAm
                ):
                    return False
        return True

    def solve(a, b):
        # next number
        # check if correct
        # else higher
        # if no number possible last changed number one higher
        xIdx = a
        yIdx = b
        ruleBreak = False
        while xIdx < 9 and yIdx < 9:
            if keyboard.is_pressed("q"):
                printBoard()
                break
            if not given[xIdx][yIdx]:
                # do while in python
                while True:
                    board[xIdx][yIdx] = board[xIdx][yIdx] + 1
                    time.sleep(0.1)
                    print(
                        f"Koordinates are {xIdx} {yIdx}, tried value is {board[xIdx][yIdx]}"
                    )
                    if board[xIdx][yIdx] == 10:
                        board[xIdx][yIdx] = 0
                        time.sleep(0.1)
                        if xIdx > 0:
                            # print("go one back x")
                            xIdx = xIdx - 1
                            while given[xIdx][yIdx]:
                                if not xIdx == 0:
                                    xIdx = xIdx - 1
                                elif not yIdx == 0:
                                    xIdx = 8
                                    yIdx = yIdx - 1
                            break
                        else:
                            # print("go one back y")
                            xIdx = 8
                            yIdx = yIdx - 1
                            while given[xIdx][yIdx]:
                                if not xIdx == 0:
                                    xIdx = xIdx - 1
                                elif not yIdx == 0:
                                    xIdx = 8
                                    yIdx = yIdx - 1
                            break
                    if SudokuGame.checkRules(xIdx, yIdx):
                        ruleBreak = True
                        break
            if ruleBreak:
                if xIdx < 8:
                    xIdx = xIdx + 1
                else:
                    xIdx = 0
                    yIdx = yIdx + 1
                ruleBreak = False
            if given[xIdx][yIdx]:
                if xIdx < 8:
                    xIdx = xIdx + 1
                else:
                    xIdx = 0
                    yIdx = yIdx + 1


for x in range(0, 9):
    for y in range(0, 9):
        print(board[x][y], end=" ")
        if board[x][y] != 0:
            given[x][y] = True
        else:
            given[x][y] = False
    print("\n")

root = Tk()
SudokuGUI(root, board)
root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
root.mainloop()


# SudokuGame.solve(0,0)

print(
    "\n\n--------------------------------------------------------------------------------\n\n"
)

for x in range(0, 9):
    for y in range(0, 9):
        print(board[x][y], end=" ")
    print("\n")
