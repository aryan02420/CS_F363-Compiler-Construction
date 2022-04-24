#! tetris-lang

// start screen
initialize_tetris_window(20, 10);

// logo
var logo_path:='/home/hardik/tetris.png';
set_logo(logo_path);

//sound
var sound_path:='/home/hardik/tetris.mp3';
set_sound(sound_path);

// add block
var newBlock := createBlock([[5,6,9],
[5,6,10],
[6,9,10],
[5,9,10]],
[255,0,0]);

add_block(newBlock);

// levels
var levels:=3;
set_levels(levels);

// keyboard config

// main game logo
var play_again := True;
var run := True;
while play_again do
begin
    //main menu
    show_main_menu();

    while run do
    begin
        update_clock();
        get_new_shape();

        if lost then
        begin
            run:=False;
        end
    end
    
    play_again:=show_game_over();
end