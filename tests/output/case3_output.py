#!/usr/bin/env python

import sys
from tetrislang import TetrisEngine

engine = TetrisEngine()

def Game():

    def new_func(arg):

        if arg != 0:
            engine.set_window_caption("Score : " + str(arg))

    engine.initialize_window(18, 10)
    temp_block = [[['.....', '.....', '..0..', '..0..', '.....'], ['.....', '..00.', '.....', '.....', '.....']], [128, 165, 0], 'new']
    engine.create_block(temp_block)
    engine.show_next_piece(True)
    engine.show_highscore(True)
    engine.set_level(1)
    engine.increase_fall_speed(True)
    engine.set_window_caption("Start!")
    play_again = True

    while play_again:
        engine.main_menu()
        run = True
        score = 0
        engine.init_grid()
        engine.init_blocks()
        engine.init_clock()

        while run:
            engine.update_locked_grid()
            engine.update_clock()
            engine.shift_piece()
            engine.take_user_input()
            engine.draw_current_grid()

            if engine.current_piece_locked():
                engine.spawn()
                score = score + engine.clear_rows()
                new_func(score)
                engine.update_highscore(score)

            engine.update_window(score)

            if engine.check_lost():
                run = False


        engine.game_over()



if __name__ == '__main__':
    Game()
