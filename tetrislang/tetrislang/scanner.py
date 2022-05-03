from sly import Lexer

class TetrisLexer(Lexer):

    def __init__(self):
        self.engineFunctionList = ['initialize_window',
                                   'create_block',
                                   'show_next_piece',
                                   'show_highscore',
                                   'enable_shadow',
                                   'enable_hard_drop',
                                   'set_level',
                                   'set_level_fallspeed',
                                   'increase_fall_speed',
                                   'set_window_caption',
                                   'main_menu',
                                   'init_grid',
                                   'init_blocks',
                                   'init_clock',
                                   'update_locked_grid',
                                   'update_clock',
                                   'shift_piece',
                                   'take_user_input',
                                   'draw_current_grid',
                                   'current_piece_locked',
                                   'spawn',
                                   'clear_rows',
                                   'update_highscore',
                                   'update_window',
                                   'check_lost',
                                   'paused',
                                   'game_over']
        
    # Set of token names. This is always required
    tokens = {VAR, IDENT, ASSIGN, BOOL, NUM, LSQBR, RSQBR, COMMA, STRING, MUL, DIV, MOD, ADD, SUB, LT, LTEQ, GT, GTEQ, EQ, NEQ, BITNOT, SAL, SAR, BITAND, BITXOR, BITOR, NOT, AND, OR, FUNCTION, LPAREN, RPAREN, BEGIN, END, IF, ELSE, WHILE, FOR, TO, EOL, BREAK, CONTINUE, FLOAT}

    # String containing ignored characters between tokens
    ignore = ' \t\r'
    # Other ignored patterns
    ignore_comment = r'\/\/.*'

    # Define a rule so we can track line numbers
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    # Compute column.
    #     input is the input text string
    #     token is a token instance
    def find_column(self, text, token):
        last_cr = text.rfind('\n', 0, token.index)
        if last_cr < 0:
            last_cr = 0
        column = (token.index - last_cr) + 1
        return column

    # Error handling rule
    def error(self, t):
        print('Line %d, Col %d: Bad character %r' % (self.lineno, self.find_column(self.text, t), t.value[0]))
        self.index += 1

    # Regular expression rules for tokens
    IDENT = r'[a-zA-Z][a-zA-Z0-9_]*'
    ASSIGN = r'\:\='
    FLOAT = r'[0-9]+\.[0-9]+'
    NUM = r'[0-9]+'
    LSQBR = r'\['
    RSQBR = r'\]'
    COMMA = r'\,'
    STRING = r'\"[^\"]*\"|\'[^\']*\''
    MUL = r'\*'
    DIV = r'\/'
    MOD = r'\%'
    ADD = r'\+'
    SUB = r'\-'
    SAL = r'\<\<'
    SAR = r'\>\>'
    LTEQ = r'\<\='
    LT = r'\<'
    GTEQ = r'\>\='
    GT = r'\>'
    EQ = r'\=\='
    NEQ = r'\!\='
    BITNOT = r'\~'
    BITAND = r'\&'
    BITXOR = r'\^'
    BITOR = r'\|'
    LPAREN = r'\('
    RPAREN = r'\)'
    EOL = r'\;'

    IDENT['var'] = VAR
    IDENT['true'] = BOOL
    IDENT['false'] = BOOL
    IDENT['if'] = IF
    IDENT['not'] = NOT
    IDENT['and'] = AND
    IDENT['or'] = OR
    IDENT['function'] = FUNCTION
    IDENT['begin'] = BEGIN
    IDENT['else'] = ELSE
    IDENT['while'] = WHILE
    IDENT['for'] = FOR
    IDENT['to'] = TO
    IDENT['end'] = END
    IDENT['continue'] = CONTINUE
    IDENT['break'] = BREAK

    @_(r'[a-zA-Z][a-zA-Z0-9_]*')
    def IDENT(self, t):
        if t.value in self.engineFunctionList:
            t.value = f'engine.{t.value}'
        return t



if __name__ == '__main__':
    data = '''
        var a := b;
        l = m;
        if (1) begin lol(); end ok();
    '''

    lexer = TetrisLexer()

    while(data[-3:] != 'EOF'):
        try:
            for tok in lexer.tokenize(data):
                print(tok)
            data = input('>> ')

        except Exception as e:
            print(e)
        

