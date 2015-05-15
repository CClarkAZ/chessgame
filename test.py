from Board import Board

test_str3 = "r2q1rk1/pp2bppp/2p1pn2/3pP1B1/8/2N1PP1P/PPP1Q1P1/R4RK1"

a = Board()
a.loadFromFEN(test_str3)
a.printBoard(0)
print ""
a.movePiece("e2", "d1")
a.printBoard(0)
