class GameBoard(object):
    def __init__(self, battleships, width, height) -> None:
        self.battleships = battleships;
        self.shots = [];
        self.width = width;
        self.height = height;

    def take_shot(self, shot_location):
        is_hit = False;
        for b in self.battleships:
            idx = b.body_index(shot_location);
            if idx is not None:
                is_hit = True;
                b.hits[idx] = True;
                break;
        
        self.shots.append(Shot(shot_location, is_hit));
    
    def is_game_over(self):
        for b in self.battleships:
            if not b.is_destroyed():
                return False
        return True

            

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
    
    def is_destroyed(self):
        return all(self.hits)
        
def renderGame(game_board, show_battleships = False):
    display = '+' + '-' * game_board.width + "+";

    print(display);

    #Construct empty board
    board = [];
    for _ in range(game_board.width):
        row = []
        for _ in range(game_board.height):
            row.append(None);
        board.append(row);

     #Actually put values(Battleship) in the empty board
    if show_battleships:
        for b in game_board.battleships:
            for x, y in b.body:
                board[x][y] = "O";
        
    for sh in game_board.shots:
        x, y = sh.location
        if sh.is_hit:
            ch = "X"
        else:
            ch = "."
        board[x][y] = ch;
    
    for y in range(game_board.height):
        row = [];
        for x in range(game_board. width):
            row.append(board[x][y] or " ")
        print("|" + "".join(row) + "|")

    print(display);



if __name__ == '__main__':
    battleships = [BattleShip.build((1,1), 2, "N"),
                   #BattleShip.build((5,8), 5, "N"),
                   #BattleShip.build((2,3), 4, "E")
                   ]

    game_board = GameBoard(battleships, 10, 10);

    while True:
        #TODO: deal with invalid inputs 
        inp = input("Where do you want to shoot?\n");
        xStr, yStr = inp.split(",");
        x = int(xStr);
        y = int(yStr);

        game_board.take_shot((x,y))
        renderGame(game_board)

        if game_board.is_game_over():
            print("YOU WIN!");
            break



