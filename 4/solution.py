from functionality import read_input, BingoBoards

filename = "input.txt"
drawn_numbers, matrices = read_input(filename, n_matrices=100)

BingoBoard = BingoBoards(matrices)

for number in drawn_numbers:
    BingoBoard.mark_boards(number)
    bingo = BingoBoard.check_boards()
    if bingo:
        board_score = BingoBoard.get_board_score()
        total_score = board_score * number
        break

# Solution is 45031.0
print(f"Winning Board: {BingoBoard.bingoboard}")
print(f"Winning Score: {total_score}")

filename = "input.txt"
drawn_numbers, matrices = read_input(filename, n_matrices=100)
# In the second part we want to figure out which one wins last
BingoBoard = BingoBoards(matrices)
last_bingoboard = -1
for number in drawn_numbers:
    BingoBoard.mark_boards(number)
    bingo = BingoBoard.check_boards()
    if bingo and BingoBoard.bingoboard != last_bingoboard:
        board_score = BingoBoard.get_board_score()
        total_score = board_score * number
        last_bingoboard = BingoBoard.bingoboard


# 14212 is too high.
print(f"Loosing Board: {BingoBoard.bingoboard}")
print(f"Loosing Score: {total_score}")
