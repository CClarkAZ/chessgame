
def setB(x, y, board, val):
	board[8*y + x] = val

def getB(x, y, board):
	return str(board[8*y + x])

def parseFENBoard(string):
	rank_strings = list(reversed(string.split('/'))) # want white pieces to be start of array
	assert(len(rank_strings) == 8)

	output = ['~' for x in range(64)]

	for rank_index, rank in enumerate(rank_strings):
		ind = 0
		for i in range(len(rank)):
			if rank[i].isdigit():
				ind += int(rank[i])
			else:
				setB(ind, rank_index, output, rank[i])
				ind += 1

	return output

def boardToFEN(board):
	# board is a list of Piece objects, each containing their respective FEN representations, starting with white pieces (rank 1)
	empty_count = 0
	moves = []
	for i in range(8):
		temp = []
		for j in range(8):
			if getB(j, i, board) == '~':
				empty_count += 1
			else:
				if empty_count > 0:
					temp.append(str(empty_count))
					empty_count = 0
				temp.append(getB(j, i, board))
		if empty_count > 0:
			temp.append(str(empty_count))
			empty_count = 0
		temp.append('/')
		moves = temp + moves
	moves.pop()

	return "".join(moves)
	


def main():
	test_str = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
	test_str2 = "1r2r2k/1p1n3R/p1qp2pB/6Pn/P1Pp4/3B4/1P2PQ1K/5R2"




	b1 = parseFENBoard(test_str)
	assert(test_str == boardToFEN(b1))


	b2 = parseFENBoard(test_str2)
	assert(test_str2 == boardToFEN(b2))

if __name__ == '__main__':
	main()
