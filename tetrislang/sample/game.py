#!/usr/bin/env python

import sys
from tetrislang import TetrisEngine

engine = TetrisEngine()

def Game():

    engine.initialize_window(18, 10)
    temp_block = [[['.....', '..0..', '.000.', '..0..', '.....']], [255, 255, 255], 'x']
    engine.create_block(temp_block)
    engine.show_next_piece(True)
    engine.show_highscore(True)
    engine.increase_fall_speed(True)
    speed_list = [0.55, 0.35, 0.15]
    engine.set_level_fallspeed(speed_list)
    engine.set_window_caption("Tetris by BlockBusters")
    engine.enable_hard_drop(True)
    engine.enable_shadow(True)
    play_again = True
    level = 0

    while play_again:
        level = engine.main_menu()
        engine.set_level(level)
        run = True
        restart = False
        score = 0
        engine.init_grid()
        engine.init_blocks()
        engine.init_clock()

        while run:
            engine.update_locked_grid()
            engine.update_clock()
            engine.shift_piece()

            if engine.take_user_input():
                restart = engine.paused()

                if restart:
                    break



            engine.draw_current_grid()

            if engine.current_piece_locked():
                engine.spawn()
                score = score + engine.clear_rows()
                engine.update_highscore(score)

            engine.update_window(score)

            if engine.check_lost():
                run = False



        if restart:
            continue

        else:
            play_again = engine.game_over()




if __name__ == '__main__':
    Game()
