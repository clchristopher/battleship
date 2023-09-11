class Battleship(object):
    @staticmethod
    def build(head, length, direction):
        body = []
        #start with empty list, then add on
        for i in range(length):
            if direction == 'N':
                el = (head[0], head[1] - i)
                #it is minus because going down, is going up in y cordinate, (0,0) to (9,9)
            elif direction == 'S':
                el = (head[0], head[1] + i)
            elif direction == 'W':
                el = (head[0] - i, head[1])
            else:
                el = (head[0] + i, head[1])

            body.append(el)
        return Battleship(body)
    #get the starting point, which direction it points, and how long it is, then convert it to a battleship body

    def __init__(self, body):
        self.body = body


##rendering board
def render(board_width, board_height, attempts):
    header = "+" + "-" * (board_width) + "+"
    ## means we have to change it less
    print(header)
    shots_set = set(attempts)
    #shots is currently a list, so we change it to a set which is faster to work with, since order dont matter
    for y in range(board_height):
        row = []
        #setting empty list, and then adding in
        for x in range(board_width):
            if (x,y) in shots_set:
                ch = "X"
            else:
                ch = " "
            row.append(ch)
        print("|" + "".join(row) + "|")
#",".join[row], takes a list and turns it to a string with , seperating it like the csv files for anki
    print(header)

def render_battleships(board_width, board_height, battleships):
    header = "+" + "-" * (board_width) + "+"
    print(header)

    #using a 2d list, each element is a list, creating a 2d list with all none, and then changing it if it is a boat

    board = []
    for _ in range(board_width):
        board.append([None for _ in range(board_height)])

    #add battleship to board
    for b in battleships:
        for x, y in b.body:
            board[x][y] = "O"

    for i in range(board_height):
        row = []
        for j in range(board_width):
            row.append((board[j][i]) or " ")
                                    # this or " " is what you fill in None with, notation
        print("|" + "".join(row) + "|")
    print(header)



if __name__ == "__main__":
    battleships = [
        Battleship.build((1,1), 2, "N"),
        Battleship.build((5,8), 5, "N"),
        Battleship.build((2,3), 4, "E"),
    ]
    for b in battleships:
        print(b.body)

    render_battleships(10,10, battleships)


    print("Hello World!")
    shots = []
    #list which we will later turn to a set
    while True:
        inp = input("Where do you want to shoot?\n")
        #deal with invalid ones later
        xstr,ystr = inp.split(",") #.split method uses whats in () as where to cut or split it
        #*,* = is assignment notation, assigns each to part of list
        x = int(xstr)
        y = int(ystr)

        shots.append((x,y))
        render(10,10, shots)
