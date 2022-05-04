initialize_window(18, 10)
var temp_block := [
    [['.....',
    '..0..',
    '.000.',
    '..0..',
    '.....']],[255,255,255], 'x'];

create_block(temp_block);
show_next_piece(True)
show_highscore(True);
increase_fall_speed(True);
var speed_list := [0.55, 0.35, 0.15]
set_level_fallspeed(speed_list);
set_window_caption("Tetris by BlockBusters");
enable_hard_drop(True)
enable_shadow(True);

var play_again := True;
var level := 0


while (play_again)
begin 
    level := main_menu();
    set_level(level);

    var run := True
    var restart := False;
    var score := 0;

    init_grid();
    init_blocks();
    init_clock();
    while (run)
    begin
        update_locked_grid();
        update_clock()
        shift_piece();
        
        if (take_user_input())
        begin
            restart := paused();
            if (restart)
            begin
                break
            end
        end
        
        draw_current_grid();

        if (current_piece_locked())
        begin
            spawn();
            score := score + clear_rows();
            update_highscore(score);
        end

        update_window(score);

        if (check_lost())
        begin
            run := False
        end
    end
    if(restart)
    begin
        continue;
    end
    else
    begin
        play_again := game_over();
    end
end

