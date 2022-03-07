from sly import Lexer


class CalcLexer(Lexer):
    # Set of token names.   This is always required
    tokens = {VAR, IDENT, ASSIGN, BOOL, NUM, LSQBR, RSQBR, COMMA, STRING, MUL, DIV, MOD, ADD, SUB,
              LT, LTEQ, GT, GTEQ, EQ, NEQ, BITNOT, SAL, SAR, BITAND, BITXOR, BITOR, NOT, AND, OR,
              FUNCTION, LPAREN, RPAREN, BEGIN, END, IF, THEN, ELSE, WHILE, DO, FOR, TO, EOL}

    # String containing ignored characters between tokens
    ignore = ' \t'
    # Other ignored patterns
    ignore_comment = r'\/\/.*'

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


if __name__ == '__main__':
    data = input()
    lexer = CalcLexer()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))

