class BattleShip(object):   
    #method you call on the class
    @staticmethod
    def build(head, length, direction):
        body = [];
        for i in range(length):
            if direction == 'N':
                el = (head[0], head[1] - i);
            elif direction == 'S':
                el = (head[0], head[1] + i);
            elif direction == 'W':
                el = (head[0] - i, head[1]);
            elif direction == 'E':
                el = (head[0] + i, head[1]);

            body.append(el)
        return BattleShip(body);
            
    def __init__(self, body):
        self.body = body;

def renderBoard(board_width, board_height, shots):
    display = '+' + '-' * board_width + "+";

    print(display);

    shots_set = set(shots);
    for y in range(board_height):
        row = '';
        for x in range(board_width):
            if (x, y) in shots_set:
                ch = 'X';
            else:
                ch = ' ';
            row += ch;
        print('|' + row + '|');
    print(display);

def renderBattleShips(board_width, board_height, battleships):
     display = '+' + '-' * board_width + "+";

     print(display);

    #Construct empty board
     board = [];
     for _ in range(board_width):
        row = []
        for _ in range(board_height):
            row.append(None);
        board.append(row);

     #Actually put values(Battleship) in the empty board
     for b in battleships:
        for x, y in b.body:
            board[x][y] = "O";
    
     for y in range(board_height):
        row = [];
        for x in range(board_width):
            row.append(board[x][y] or " ")
        print("|" + "".join(row) + "|")

     print(display);


if __name__ == '__main__':
    battleships = [BattleShip.build((1,1), 2, "N"),
                   BattleShip.build((5,8), 5, "N"),
                   BattleShip.build((2,3), 4, "E")
                   ]

    for b in battleships:
        print(b.body);

    renderBattleShips(10, 10, battleships);

    exit(0);


    shots = [];

    while True:
        #TODO: deal with invalid inputs 
        inp = input("Where do you want to shoot?\n");
        xStr, yStr = inp.split(",");
        x = int(xStr);
        y = int(yStr);

        shots.append((x,y));
        renderBoard(10, 10, shots)

