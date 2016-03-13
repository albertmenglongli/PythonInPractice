# BLACK, WHITE = ("BLACK", "WHITE")
#
# class AbstractBoard(object):
#     def __init__(self, rows, columns):
#         self.board=[[None for _ in range(columns)] for _ in range(rows)]
#         self.populate_board()
#
#     def populate_board(self):
#         raise NotImplementedError()
#
#     def __str__(self):
#         squares = []
#         for y, row in enumerate(self.board):
#             for x, piece in enumerate(row):
#                 square = console(piece, BLACK if (y+x)%2 else WHITE)
#                 squares.append(square)
#             squares.append("\n")
#         return "".join(squares)
#
# class CheckersBoard(AbstractBoard):
#     def __init__(self):
#         super(CheckersBoard, self).__init__(10,10)
#
#     def populate_board(self):
#         for x in range(0,9,2):
#             for row in range(4):
#                 column = x+((row+1)%2)
#                 self.board[row][column]=Bl
#
# def main():
#     checkers = CheckersBoard()
#     print (checkers)
#
#     chess = ChessBoard()
#     print(chess)

class Piece(str):
    __slots__=()

    def __new__(cls, *args, **kwargs):
        return str.__new__(cls,*args,**kwargs)

class BlackDraught(Piece):
    __slots__ = ()

    def __new__(cls, *args, **kwargs):
        new_instance = Piece.__new__(cls, "\N{black draughts man}")
        return new_instance

class WhiteDraught(Piece):
    __slots__ = ()

    def __new__(cls, *args, **kwargs):
        return Piece.__new__(cls, "\N{white draughts man}")

# very risky to write codes like this
def create_piece(kind,color):
    if kind == "Draught":
        return eval("{}{}()".format(color, kind))
    return None

BLACK, WHITE = ("BLACK", "WHITE")
DRAUGHT, = ("DRAUGHT",)
def create_piece1(kind,color):
    __PieceClass = {
        (DRAUGHT, BLACK):BlackDraught,
        (DRAUGHT, WHITE):WhiteDraught,
    }
    return __PieceClass[kind,color]()

def main():
    blackDraught = create_piece("Draught","Black")
    print(blackDraught)
    whiteDraught = create_piece("Draught","White")
    whiteDraught = create_piece1(DRAUGHT,WHITE)
    print(whiteDraught)
    print(isinstance(blackDraught,Piece))
    print(isinstance(blackDraught,BlackDraught))
    print(isinstance(blackDraught,WhiteDraught))


if __name__ == "__main__":
    main()