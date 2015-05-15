from pprint import pprint
from piece import Piece
import FEN_Util


class Board(object):
	def __init__(self):
		self.board = []

	def loadFromFEN(self, fen_moves_string): # need to update this to handle full FEN string
		parsed_board = FEN_Util.parseFENBoard(fen_moves_string)
		for i, p in enumerate(parsed_board):
			parsed_board[i] = Piece(p)

		self.board = parsed_board

	def getFEN(self):
		return FEN_Util.boardToFEN(self.board)

	def getAt(self, x, y):
		return self.board[8 * x + y]

	def setAt(self, x, y, set_to):
		self.board[8 * x + y] = set_to

	def fromAlgToIndex(self, rank, f):
		a = rank.upper()
		trans = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7}
		return (f-1, trans[a])

	def getPieceFromAlg(self, rank, f):
		p = self.fromAlgToIndex(rank, f)
		return self.getAt(p[0], p[1])


	def movePieceByCoordinates(self, s_rank, s_f, d_rank, d_f):
		i_coord = self.fromAlgToIndex(s_rank, s_f)
		f_coord = self.fromAlgToIndex(d_rank, d_f)

		p_to_move = self.getPieceFromAlg(s_rank, s_f)
		self.setAt(f_coord[0], f_coord[1], p_to_move)
		self.setAt(i_coord[0], i_coord[1], Piece('~'))

	def movePiece(self, initial, final):
		# for example, "d1", "d2"
		if len(initial) != 2 or len(final) != 2:
			raise ValueError("Moves must be 2 characters long")
		i = list(initial)
		f = list(final)

		self.movePieceByCoordinates(i[0], int(i[1]), f[0], int(f[1]))


	def printBoard(self, orientation=1): # 1 for normal, 0 for reversed
		if orientation == 0:
			for i in range(8):
				temp = ""
				for j in range(7,-1,-1):
					temp += str(self.getAt(i, j)) + " "
				print temp

		else:
			for i in range(7,-1,-1):
				temp = ""
				for j in range(8):
					temp += str(self.getAt(i, j)) + " " 
				print temp


def main():
	board = Board()
	board.loadFromFEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
	board.printBoard()


if __name__ == '__main__':
	main()