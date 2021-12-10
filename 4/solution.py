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

print(f"Winning Board: {BingoBoard.bingoboard}")
print(f"Winning Score: {total_score}")

