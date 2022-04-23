import TLGameEngine

TLGameEngine.initialize_tetris_window(20, 10);

var1 = '/home/hardik/tetris.png'
TLGameEngine.set_logo(var1)

var2 = '/home/hardik/tetris.mp3'
TLGameEngine.set_logo(var1)

var3 = TLGameEngine.createBlock([[5,6,9],
[5,6,10],
[6,9,10],
[5,9,10]],
[255,0,0])

TLGameEngine.add_block(var3)

var4 = 3

TLGameEngine.set_levels(var4)

var4 = True
var5 = True

while var4 :
    TLGameEngine.show_main_menu()
    while var5 :
        TLGameEngine.update_clock()
        TLGameEngine.get_new_shape()

        if TLGameEngine.check_lost():
            var5 = False
    
    var4 = TLGameEngine.show_game_over()
