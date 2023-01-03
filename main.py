import copy
import random

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
        return BattleShip(body, direction);
            
    def __init__(self, body, head, length, direction):
        self.body = body;
        self.direction = direction
        self.hits = [False] * len(body);

    def body_index(self, location):
        try:
            return self.body.index(location);
        except ValueError:
            return None;
    
    def is_destroyed(self):
        return all(self.hits)


class Player(object):
    def __init__(self, name, shot_f):
        self.name = name;
        self.shot_f = shot_f;


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
            for i, (x, y) in enumerate(b.body):
                if b.direction == "N":
                    chs = ('v', '|', 'ʌ')
                elif b.direction == "S":
                    chs = ('ʌ', '|', 'v')
                elif b.direction == "W":
                    chs = ('>', '-', '<')
                elif b.direction == "E":
                    chs = ('<', '-', '>')
                else:
                    raise "Unknown Direction"
                
                if i == 0:
                    ch = chs[0];
                elif i == len(b.body) - 1:
                    ch = chs[2]
                else:
                    ch = chs[1]
                
                board[x][y] = ch

        
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

def get_random_ai_shot(game_board):
    x = random.randint(0, game_board.width - 1)
    y = random.randint(0, game_board.height - 1)
    return (x, y)

def get_human_shot(game_board):
     inp = input("Where do you want to shoot?\n");
     xStr, yStr = inp.split(",");
     x = int(xStr);
     y = int(yStr);
     return (x, y)

    



if __name__ == '__main__':
    
    battleships = [BattleShip.build((1,1), 2, "S"),
                   BattleShip.build((5,8), 5, "N"),
                   BattleShip.build((2,3), 4, "E")
                   ]

    game_boards = [GameBoard(battleships, 10, 10),
                   GameBoard(copy.deepcopy(battleships), 10, 10),
                   ];

    players = [Player('Rob', get_human_shot),
               Player('Alice', get_random_ai_shot)]
    
    off_idx = 0;

    while True:
        def_idx = (off_idx + 1) % 2; 

        defensive_board = game_boards[def_idx];
        offensive_player = players[off_idx];
        #TODO: deal with invalid inputs 

        print("%s YOUR TURN!" % offensive_player.name)
        shot_location = offensive_player.shot_f(defensive_board)
        
        defensive_board.take_shot(shot_location)
        renderGame(defensive_board)

        if defensive_board.is_game_over():
            print("%s WINS!" % offensive_player.name);
            break

        off_idx = def_idx;


