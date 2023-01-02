class GameBoard(object):
    def __init__(self, battleships, board_width, board_height) -> None:
        self.battleships = battleships;
        self.shots = [];
        self.board_width = board_width;
        self.board_height = board_height;

    def take_shot(self, shot_location):
        is_hit = False;
        for b in self.battleships:
            idx = b.body_index(shot_location);
            if idx is not None:
                is_hit = True;
                b.hits[idx] = True;
                break;
        
        self.shots.append(Shot(shot_location, is_hit));
            

class Shot(object):
    def __init__(self, location, is_hit):
        self.location = location;
        self.is_hit = is_hit;



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
        self.hits = [False] * len(body);

    def body_index(self, location):
        try:
            return self.body.index(location);
        except ValueError:
            return None;
        

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

    game_board = GameBoard(battleships, 10, 10);
    shots = ((1,1), (0,0), (5, 7))
    for sh in shots:
        game_board.take_shot(sh)

    for sh in game_board.shots:
        print(sh.location)
        print(sh.is_hit)
        print("========")
    for b in game_board.battleships:
        print(b.body)
        print(b.hits)
        print('========')

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

