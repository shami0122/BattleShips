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


if __name__ == '__main__':
    shots = [];

    while True:
        #TODO: deal with invalid inputs 
        inp = input("Where do you want to shoot?\n");
        xStr, yStr = inp.split(",");
        x = int(xStr);
        y = int(yStr);

        shots.append((x,y));
        renderBoard(10, 10, shots)

