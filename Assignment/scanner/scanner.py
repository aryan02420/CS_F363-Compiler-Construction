from sly import Lexer

class CalcLexer(Lexer):
    # Set of token names. This is always required
    tokens = {VAR, IDENT, ASSIGN, BOOL, NUM, LSQBR, RSQBR, COMMA, STRING, MUL, DIV, MOD, ADD, SUB, LT, LTEQ, GT, GTEQ, EQ, NEQ, BITNOT, SAL, SAR, BITAND, BITXOR, BITOR, NOT, AND, OR, FUNCTION, LPAREN, RPAREN, BEGIN, END, IF, THEN, ELSE, WHILE, DO, FOR, TO, EOL}

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
    def find_column(text, token):
        last_cr = text.rfind('\n', 0, token.index)
        if last_cr < 0:
            last_cr = 0
        column = (token.index - last_cr) + 1
        return column

    # Error handling rule
    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1

    # Regular expression rules for tokens
    IDENT = r'[a-zA-Z][a-zA-Z0-9_]*'
    ASSIGN = r'\:\='
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
    LT = r'\<'
    LTEQ = r'\<\='
    GT = r'\>\='
    GTEQ = r'\<\='
    EQ = r'\='
    NEQ = r'\!\='
    BITNOT = r'\~'
    SAL = r'\<\<'
    SAR = r'\>\>'
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
    IDENT['then'] = THEN
    IDENT['else'] = ELSE
    IDENT['while'] = WHILE
    IDENT['do'] = DO
    IDENT['for'] = FOR
    IDENT['to'] = TO
    IDENT['end'] = END


if __name__ == '__main__':
    data = input()

    try:
        while(data[-3:] != 'EOF'):
            lexer = CalcLexer()
            for tok in lexer.tokenize(data):
                print('type=%r, value=%r' % (tok.type, tok.value))

            data = input()

    except:
        print("Scanning Done!")
        

