initialize_window(18, 10);
var temp_block := [
    [['.....',
    '.....',
    '..0..',
    '..0..',
    '.....'],
    ['.....',
    '..00.',
    '.....',
    '.....',
    '.....']],(128,165,0)];

create_block(temp_block);
show_next_piece(True);
show_highscore(True);
set_level(1);
increase_fall_speed(True);
set_window_caption("Hardik :)");

play_again := True;

while (play_again)
begin 
    main_menu();

    var run := True;
    var score := 0;

    init_grid();
    init_blocks();
    init_clock();
    while (run)
    begin
        update_locked_grid();
        update_clock();
        shift_piece();
        take_user_input();
        draw_current_grid();

        if (current_piece_locked())
        begin
            spawn();
            score := score + clear_rows();
          update_highscore(score);
        end;

        update_window(score);

        if (check_lost())
        begin
            run := False;
        end;
    end;
    game_over();
end;

