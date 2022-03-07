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
    VAR = r'var'
    IDENT = r'[a-zA-Z][a-zA-Z0-9_]*'
    ASSIGN = r'\:\='
    BOOL = r'true|false'
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
    NOT = r'not'
    AND = r'and'
    OR = r'or'
    FUNCTION = r'function'
    LPAREN = r'\('
    RPAREN = r'\)'
    BEGIN = r'begin'
    END = r'end'
    IF = r'if'
    THEN = r'then'
    ELSE = r'else'
    WHILE = r'while'
    DO = r'do'
    FOR = r'for'
    TO = r'to'
    EOL = r'\;'


if __name__ == '__main__':
    data = '''
      var x := 3 + 42 * (s - t);
      true = false;
    '''
    lexer = CalcLexer()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))
