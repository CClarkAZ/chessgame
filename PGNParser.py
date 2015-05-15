import re
from PGNParseError import PGNParseError
from Graph import Node


with open('game.txt') as game_file:
	pgn_str = game_file.read()

def chunks(l, n):
	for i in xrange(0, len(l), n):
		yield l[i:i+n]


def parseMoves(moves_string):
	# returns move tree
	try:
		moves_string = removeComments(moves_string)
	except PGNParseError as e:
		print "Error parsing PGN at position %i\n" % e.error_pos
	else:
		moves_string = formatPGNString(moves_string)

		tokens = moves_string.split(' ')
		tokens.pop()
		moveList = list(chunks(tokens, 3))
		
		root = Node()


def removeComments(moves_string):
	# comments are either semicolon that continues to end of line, or brackets {}
	while ';' in moves_string:
		i = moves_string.find(';')
		j = moves_string.find('\n', i)
		if j < 0:
			j = len(moves_string)
		moves_string = moves_string[:i] + moves_string[j:]

	while '{' in moves_string:
		i = moves_string.find('{')
		j = moves_string.find('}')
		if j < 0:
			raise PGNParseError(j)
		moves_string = moves_string[:i] + moves_string[(j+1):]

	return moves_string

def formatPGNString(moves_string):
	moves_string = moves_string.replace('\n', ' ')
	return moves_string.replace("  ", " ")

parseMoves(pgn_str)

