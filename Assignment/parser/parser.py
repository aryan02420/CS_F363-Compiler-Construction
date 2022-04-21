from sly import Parser
import sys
sys.path.append("..")
from scanner.scanner import CalcLexer


class CalcParser(Parser):
    # Get the token list from the lexer (required)
    tokens = CalcLexer.tokens

    @_('statements EOL')
    def program(self, p):
        pass

    @_('statement ( EOL statement ) *')
    def statements(self, p):
        pass

    @_('assignmentStatement')
    def statement(self, p):
        pass

    @_('variableDeclaration')
    def statement(self, p):
        pass

    @_('functionStatement')
    def statement(self, p):
        pass

    @_('functionDeclaration')
    def statement(self, p):
        pass

    @_('compoundStatement')
    def statement(self, p):
        pass

    @_('conditionalStatement')
    def statement(self, p):
        pass

    @_('loopStatement')
    def statement(self, p):
        pass

    @_('emptyStatement')
    def statement(self, p):
        pass

    @_('IDENT ASSIGN expression')
    def assignmentStatement(self, p):
        pass

    @_('IDENT LPAREN RPAREN')
    def functionStatement(self, p):
        pass
    
    @_('IDENT LPAREN actparams RPAREN')
    def functionStatement(self, p):
        pass

    @_('expression (COMMA expression)*')
    def actparams(self, p):
        pass

    @_('BEGIN statements END')
    def compoundStatement(self, p):
        pass

    @_('IF expression THEN statement (ELSE statement)*')
    def conditionalStatement(self, p):
        pass

    @_('WHILE expression DO statement')
    def loopStatement(self, p):
        pass

    @_('DO statement WHILE expression')
    def loopStatement(self, p):
        pass

    @_('FOR IDENT ASSIGN number TO number DO statement')
    def loopStatement(self, p):
        pass

    @_('/*empty*/')
    def emptyStatement(self, p):
        pass

    @_('VAR IDENT ASSIGN expression')
    def variableDeclaration(self, p):
        pass

    @_('FUNCTION IDENT LPAREN RPAREN compoundStatement')
    def functionDeclaration(self, p):
        pass
    
    @_('FUNCTION IDENT LPAREN fargs RPAREN compoundStatement')
    def functionDeclaration(self, p):
        pass

    @_('IDENT')
    def fargs(self, p):
        pass
    
    @_('IDENT (COMMA IDENT)+')
    def fargs(self, p):
        pass

    @_('IDENT')
    def expression(self, p):
        pass

    @_('binop')
    def expression(self, p):
        pass

    @_('unop')
    def expression(self, p):
        pass

    @_('unop')
    def binop(self, p):
        pass

    @_('binop ADD unop')
    def binop(self, p):
        pass

    @_('binop SUB unop')
    def binop(self, p):
        pass

    @_('binop MUL unop')
    def binop(self, p):
        pass

    @_('binop DIV unop')
    def binop(self, p):
        pass

    @_('binop MOD unop')
    def binop(self, p):
        pass

    @_('binop LT unop')
    def binop(self, p):
        pass

    @_('binop LTEQ unop')
    def binop(self, p):
        pass

    @_('binop GT unop')
    def binop(self, p):
        pass

    @_('binop GTEQ unop')
    def binop(self, p):
        pass

    @_('binop EQ unop')
    def binop(self, p):
        pass

    @_('binop NEQ unop')
    def binop(self, p):
        pass

    @_('binop SAL unop')
    def binop(self, p):
        pass

    @_('binop SAR unop')
    def binop(self, p):
        pass

    @_('binop BITAND unop')
    def binop(self, p):
        pass

    @_('binop BITOR unop')
    def binop(self, p):
        pass

    @_('binop BITXOR unop')
    def binop(self, p):
        pass

    @_('binop AND unop')
    def binop(self, p):
        pass

    @_('binop OR unop')
    def binop(self, p):
        pass

    @_('term')
    def unop(self, p):
        pass

    @_('BITNOT term')
    def unop(self, p):
        pass

    @_('NOT term')
    def unop(self, p):
        pass

    @_('NUM')
    def term(self, p):
        pass

    @_('BOOL')
    def term(self, p):
        pass

    @_('LPAREN expression RPAREN')
    def term(self, p):
        pass


if __name__ == '__main__':
    lexer = CalcLexer()
    parser = CalcParser()

    while True:
        try:
            text = input('calc > ')
            result = parser.parse(lexer.tokenize(text))
            print(result)
        except EOFError:
            break