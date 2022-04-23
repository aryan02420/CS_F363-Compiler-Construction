import random
import pygame

pygame.init()
pygame.font.init()
    
"""
10 x 20 grid
play_height = 2 * play_width

tetriminos:
    0 - S - green
    1 - Z - red
    2 - I - cyan
    3 - O - yellow
    4 - J - blue
    5 - L - orange
    6 - T - purple
"""
# class to represent each of the pieces
class Piece(object):
    def __init__(self, x, y, shape, shape_colors, shapes):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]  # choose color from the shape_color list
        self.rotation = 0                               # chooses the rotation according to index

class TetrisEngine(object):

    """
    Game Variables
    """
    s_width = 800       # window width
    s_height = 750      # window height
    
    col = 10            # 10 columns
    row = 20            # 20 rows
    block_size = 30     # size of block

    play_width = col*block_size    # play window width; 300/10 = 30 width per block
    play_height = row*block_size   # play window height; 600/20 = 30 height per block

    top_left_x = (s_width - play_width) // 2
    top_left_y = s_height - play_height - 50

    filepath = './highscore.txt'
    fontpath = './arcade.TTF'
    fontpath_mario = './mario.ttf'
    #########################################################################

    """
    Shapes
    """
    S = [['.....',
        '.....',
        '..00.',
        '.00..',
        '.....'],
        ['.....',
        '..0..',
        '..00.',
        '...0.',
        '.....']]

    Z = [['.....',
        '.....',
        '.00..',
        '..00.',
        '.....'],
        ['.....',
        '..0..',
        '.00..',
        '.0...',
        '.....']]

    I = [['.....',
        '..0..',
        '..0..',
        '..0..',
        '..0..'],
        ['.....',
        '0000.',
        '.....',
        '.....',
        '.....']]

    O = [['.....',
        '.....',
        '.00..',
        '.00..',
        '.....']]

    J = [['.....',
        '.0...',
        '.000.',
        '.....',
        '.....'],
        ['.....',
        '..00.',
        '..0..',
        '..0..',
        '.....'],
        ['.....',
        '.....',
        '.000.',
        '...0.',
        '.....'],
        ['.....',
        '..0..',
        '..0..',
        '.00..',
        '.....']]

    L = [['.....',
        '...0.',
        '.000.',
        '.....',
        '.....'],
        ['.....',
        '..0..',
        '..0..',
        '..00.',
        '.....'],
        ['.....',
        '.....',
        '.000.',
        '.0...',
        '.....'],
        ['.....',
        '.00..',
        '..0..',
        '..0..',
        '.....']]

    T = [['.....',
        '..0..',
        '.000.',
        '.....',
        '.....'],
        ['.....',
        '..0..',
        '..00.',
        '..0..',
        '.....'],
        ['.....',
        '.....',
        '.000.',
        '..0..',
        '.....'],
        ['.....',
        '..0..',
        '.00..',
        '..0..',
        '.....']]

    # index represents the shape
    shapes = [S, Z, I, O, J, L, T]
    shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
    #########################################################################

    
    def __init__(self):
        pass
    
        
    """
    initialise the grid
    """
    def create_grid(self, locked_pos={}):
        grid = [[(0, 0, 0) for x in range(self.col)] for y in range(self.row)]  # grid represented rgb tuples

        # locked_positions dictionary
        # (x,y):(r,g,b)
        for y in range(self.row):
            for x in range(self.col):
                if (x, y) in locked_pos:
                    color = locked_pos[
                        (x, y)]  # get the value color (r,g,b) from the locked_positions dictionary using key (x,y)
                    grid[y][x] = color  # set grid position to color

        return grid

    def convert_shape_format(self, piece):
        positions = []
        shape_format = piece.shape[piece.rotation % len(piece.shape)]  # get the desired rotated shape from piece

        '''
        e.g.
        ['.....',
            '.....',
            '..00.',
            '.00..',
            '.....']
        '''
        for i, line in enumerate(shape_format):  # i gives index; line gives string
            row = list(line)  # makes a list of char from string
            for j, column in enumerate(row):  # j gives index of char; column gives char
                if column == '0':
                    positions.append((piece.x + j, piece.y + i))

        for i, pos in enumerate(positions):
            positions[i] = (pos[0] - 2, pos[1] - 4)  # offset according to the input given with dot and zero

        return positions


    """
    checks if current position of piece in grid is valid
    """
    def valid_space(self, piece, grid):
        # makes a 2D list of all the possible (x,y)
        accepted_pos = [[(x, y) for x in range(self.col) if grid[y][x] == (0, 0, 0)] for y in range(self.row)]
        # removes sub lists and puts (x,y) in one list; easier to search
        accepted_pos = [x for item in accepted_pos for x in item]

        formatted_shape = self.convert_shape_format(piece)

        for pos in formatted_shape:
            if pos not in accepted_pos:
                if pos[1] >= 0:
                    return False
        return True

    """
    check if piece is out of board
    """
    def check_lost(self, positions):
        for pos in positions:
            x, y = pos
            if y < 1:
                return True
        return False


    """
    chooses a shape randomly from shapes list
    """
    def get_shape(self):
        return Piece(int(self.col/2), 0, random.choice(self.shapes), self.shape_colors, self.shapes)


    """
    draws text in the middle
    """
    def draw_text_middle(self, text, size, color, surface):
        font = pygame.font.Font(self.fontpath, size, bold=False, italic=True)
        label = font.render(text, 1, color)

        surface.blit(label, (self.top_left_x + self.play_width/2 - (label.get_width()/2), self.top_left_y + self.play_height/2 - (label.get_height()/2)))


    """
    draws the lines of the grid for the game
    """
    def draw_grid(self, surface):
        r = g = b = 120
        grid_color = (r, g, b)

        for i in range(self.row):
            # draw grey horizontal lines
            pygame.draw.line(surface, grid_color, (self.top_left_x, self.top_left_y + i * self.block_size),
                            (self.top_left_x + self.play_width, self.top_left_y + i * self.block_size))
            for j in range(self.col):
                # draw grey vertical lines
                pygame.draw.line(surface, grid_color, (self.top_left_x + j * self.block_size, self.top_left_y),
                                (self.top_left_x + j * self.block_size, self.top_left_y + self.play_height))


    """
    clear a row when it is filled
    """
    def clear_rows(self, grid, locked):
        # need to check if row is clear then shift every other row above down one
        increment = 0
        for i in range(len(grid) - 1, -1, -1):      # start checking the grid backwards
            grid_row = grid[i]                      # get the last row
            if (0, 0, 0) not in grid_row:           # if there are no empty spaces (i.e. black blocks)
                increment += 1
                # add positions to remove from locked
                index = i                           # row index will be constant
                for j in range(len(grid_row)):
                    try:
                        del locked[(j, i)]          # delete every locked element in the bottom row
                    except ValueError:
                        continue

        # shift every row one step down
        # delete filled bottom row
        # add another empty row on the top
        # move down one step
        if increment > 0:
            # sort the locked list according to y value in (x,y) and then reverse
            # reversed because otherwise the ones on the top will overwrite the lower ones
            for key in sorted(list(locked), key=lambda a: a[1])[::-1]:
                x, y = key
                if y < index:                       # if the y value is above the removed index
                    new_key = (x, y + increment)    # shift position to down
                    locked[new_key] = locked.pop(key)

        return increment


    """
    draws the upcoming piece
    """
    def draw_next_shape(self, piece, surface):
        font = pygame.font.Font(self.fontpath, 30)
        label = font.render('Next Shape', 1, (255, 255, 255))

        start_x = self.top_left_x + self.play_width + 50
        start_y = self.top_left_y + (self.play_height / 2 - 100)

        shape_format = piece.shape[piece.rotation % len(piece.shape)]

        for i, line in enumerate(shape_format):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    pygame.draw.rect(surface, piece.color, (start_x + j*self.block_size, start_y + i*self.block_size, self.block_size, self.block_size), 0)

        surface.blit(label, (start_x, start_y - 30))

        # pygame.display.update()


    """
    draws the content of the window
    """
    def draw_window(self, surface, grid, score=0, last_score=0):
        surface.fill((0, 0, 0))  # fill the surface with black

        pygame.font.init()  # initialise font
        font = pygame.font.Font(self.fontpath_mario, 65, bold=True)
        label = font.render('TETRIS', 1, (255, 255, 255))  # initialise 'Tetris' text with white

        surface.blit(label, ((self.top_left_x + self.play_width / 2) - (label.get_width() / 2), 30))  # put surface on the center of the window

        # current score
        font = pygame.font.Font(self.fontpath, 30)
        label = font.render('SCORE   ' + str(score) , 1, (255, 255, 255))

        start_x = self.top_left_x + self.play_width + 50
        start_y = self.top_left_y + (self.play_height / 2 - 100)

        surface.blit(label, (start_x, start_y + 200))

        # last score
        label_hi = font.render('HIGHSCORE   ' + str(last_score), 1, (255, 255, 255))

        start_x_hi = self.top_left_x - 240
        start_y_hi = self.top_left_y + 200

        surface.blit(label_hi, (start_x_hi + 20, start_y_hi + 200))

        # draw content of the grid
        for i in range(self.row):
            for j in range(self.col):
                # pygame.draw.rect()
                # draw a rectangle shape
                # rect(Surface, color, Rect, width=0) -> Rect
                pygame.draw.rect(surface, grid[i][j],
                                (self.top_left_x + j * self.block_size, self.top_left_y + i * self.block_size, self.block_size, self.block_size), 0)

        # draw vertical and horizontal grid lines
        self.draw_grid(surface)

        # draw rectangular border around play area
        border_color = (255, 255, 255)
        pygame.draw.rect(surface, border_color, (self.top_left_x, self.top_left_y, self.play_width, self.play_height), 4)

        # pygame.display.update()

    """
    get the high score from the file
    """
    def get_max_score(self):
        with open(self.filepath, 'r') as file:
            lines = file.readlines()        # reads all the lines and puts in a list
            score = int(lines[0].strip())   # remove \n

        return score

    """
    update the score txt file with high score
    """
    def update_score(self, new_score):
        score = self.get_max_score()

        with open(self.filepath, 'w') as file:
            if new_score > score:
                file.write(str(new_score))
            else:
                file.write(str(score))


    def main(self, window):
        locked_positions = {}
        self.create_grid(locked_positions)

        change_piece = False
        run = True
        current_piece = self.get_shape()
        next_piece = self.get_shape()
        clock = pygame.time.Clock()
        fall_time = 0
        fall_speed = 0.35
        level_time = 0
        score = 0
        last_score = self.get_max_score()

        while run:
            # need to constantly make new grid as locked positions always change
            grid = self.create_grid(locked_positions)

            # helps run the same on every computer
            # add time since last tick() to fall_time
            fall_time += clock.get_rawtime()  # returns in milliseconds
            level_time += clock.get_rawtime()

            clock.tick()  # updates clock

            if level_time/1000 > 5:    # make the difficulty harder every 10 seconds
                level_time = 0
                if fall_speed > 0.15:   # until fall speed is 0.15
                    fall_speed -= 0.005

            if fall_time / 1000 > fall_speed:
                fall_time = 0
                current_piece.y += 1
                if not self.valid_space(current_piece, grid) and current_piece.y > 0:
                    current_piece.y -= 1
                    # since only checking for down - either reached bottom or hit another piece
                    # need to lock the piece position
                    # need to generate new piece
                    change_piece = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.display.quit()
                    quit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        current_piece.x -= 1  # move x position left
                        if not self.valid_space(current_piece, grid):
                            current_piece.x += 1

                    elif event.key == pygame.K_RIGHT:
                        current_piece.x += 1  # move x position right
                        if not self.valid_space(current_piece, grid):
                            current_piece.x -= 1

                    elif event.key == pygame.K_DOWN:
                        # move shape down
                        current_piece.y += 1
                        if not self.valid_space(current_piece, grid):
                            current_piece.y -= 1

                    elif event.key == pygame.K_UP:
                        # rotate shape
                        current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                        if not self.valid_space(current_piece, grid):
                            current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)

            piece_pos = self.convert_shape_format(current_piece)

            # draw the piece on the grid by giving color in the piece locations
            for i in range(len(piece_pos)):
                x, y = piece_pos[i]
                if y >= 0:
                    grid[y][x] = current_piece.color

            if change_piece:  # if the piece is locked
                for pos in piece_pos:
                    p = (pos[0], pos[1])
                    locked_positions[p] = current_piece.color       # add the key and value in the dictionary
                current_piece = next_piece
                next_piece = self.get_shape()
                change_piece = False
                score += self.clear_rows(grid, locked_positions) * 10    # increment score by 10 for every row cleared
                self.update_score(score)

                if last_score < score:
                    last_score = score

            self.draw_window(window, grid, score, last_score)
            self.draw_next_shape(next_piece, window)
            pygame.display.update()

            if self.check_lost(locked_positions):
                run = False

        self.draw_text_middle('You  Lost', 40, (255, 255, 255), window)
        pygame.display.update()
        pygame.time.delay(2000)  # wait for 2 seconds
        pygame.quit()
        quit()


    def main_menu(self, window):
        run = True
        while run:
            self.draw_text_middle('Press   any   key   to   begin', 50, (255, 255, 255), window)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    self.main(window)

        pygame.quit()


if __name__ == '__main__':

    root = TetrisEngine()
    win = pygame.display.set_mode((root.s_width, root.s_height))
    pygame.display.set_caption('Tetris')

    root.main_menu(win)  # start game
