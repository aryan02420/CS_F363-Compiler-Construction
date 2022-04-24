from sly import Parser
import sys
sys.path.append("..")
from scanner.scanner import CalcLexer


class CalcParser(Parser):
    debugfile = 'parser.out'
    tokens = CalcLexer.tokens

    start = 'program'

    def __init__(self):
        self.depth = 0

    @_('statements')                                                          
    def program(self, p):
        return f'{p.statements}'

    @_('statement EOL statements')                                                
    def statements(self, p):
        return f'{p.statement}\n{p.statements}'

    @_('statement EOL')                                                               
    def statements(self, p):
        return f'{p.statement}'

    @_('compoundStatement')                                                       
    def statements(self, p):
        return f'{p.compoundStatement}'

    @_('conditionalStatement')                                                    
    def statements(self, p):
        return f'{p.conditionalStatement}'

    @_('loopStatement')                                                           
    def statements(self, p):               
        return f'{p.loopStatement}'

    @_('functionDeclaration')                                                     
    def statements(self, p):               
        return f'{p.functionDeclaration}'

    @_('emptyStatement')                                                          
    def statement(self, p):
        return f'{p.emptyStatement}'

    @_('assignmentStatement')                                                     
    def statement(self, p):
        return f'{p.assignmentStatement}'

    @_('variableDeclaration')                                                     
    def statement(self, p):
        return f'{p.variableDeclaration}'

    @_('functionStatement')                                                       
    def statement(self, p):
        return f'{p.functionStatement}'

    @_('IDENT ASSIGN expression')                                                 
    def assignmentStatement(self, p):
        return f'\t'*int(p.IDENT[-1]) + f'{p.IDENT[:-1]} = {p.expression}'

    @_('IDENT LSQBR expression RSQBR ASSIGN expression')                                                 
    def assignmentStatement(self, p):
        return f'\t'*int(p.IDENT[-1]) + f'{p.IDENT[:-1]}[{p.expression0}] = {p.expression1}'

    @_('IDENT LSQBR expression SLICE expression RSQBR ASSIGN expression')                                                 
    def assignmentStatement(self, p):
        return f'\t'*int(p.IDENT[-1]) + f'{p.IDENT[:-1]}[{p.expression0} : {p.expression1}] = {p.expression2}'

    @_('IDENT LPAREN RPAREN')                                                     
    def functionStatement(self, p):
        return f'\t'*int(p.IDENT[-1]) + f'{p.IDENT[:-1]}()'

    @_('IDENT LPAREN fargs RPAREN')                                           
    def functionStatement(self, p):
        return f'\t'*int(p.IDENT[-1]) + f'{p.IDENT[:-1]}({p.fargs})'

    @_('BEGIN statements END')                                                    
    def compoundStatement(self, p):
        return f'{p.statements}\n'

    @_('IF LPAREN expression RPAREN compoundStatement')                                           
    def conditionalStatement(self, p):
        return f'\t'*p.IF + f'if {p.expression}:\n{p.compoundStatement}'

    @_('IF LPAREN expression RPAREN compoundStatement ELSE compoundStatement')                           
    def conditionalStatement(self, p):
        return f'\t'*p.IF + f'if {p.expression}:\n{p.compoundStatement0}else:{p.compoundStatement1}'
    
    @_('WHILE LPAREN expression RPAREN compoundStatement')                                           
    def loopStatement(self, p):           
        return f'\t'*p.WHILE + f'while {p.expression}:\n{p.compoundStatement}'

    @_('FOR LPAREN IDENT ASSIGN NUM TO NUM RPAREN compoundStatement')                          
    def loopStatement(self, p):           
        return f'\t'*p.FOR + f'for {p.IDENT[:-1]} in range({p.NUM0}, {p.NUM1}):\n{p.compoundStatement}'

    @_('FOR LPAREN IDENT ASSIGN IDENT TO NUM RPAREN compoundStatement')                          
    def loopStatement(self, p):           
        return f'\t'*p.FOR + f'for {p.IDENT0[:-1]} in range({p.IDENT1[:-1]}, {p.NUM}):\n{p.compoundStatement}'

    @_('FOR LPAREN IDENT ASSIGN NUM TO IDENT RPAREN compoundStatement')                          
    def loopStatement(self, p):           
        return f'\t'*p.FOR + f'for {p.IDENT0[:-1]} in range({p.NUM}, {p.IDENT1[:-1]}):\n{p.compoundStatement}'

    @_('FOR LPAREN IDENT ASSIGN IDENT TO IDENT RPAREN compoundStatement')                          
    def loopStatement(self, p):           
        return f'\t'*p.FOR + f'for {p.IDENT0[:-1]} in range({p.IDENT1[:-1]}, {p.IDENT2[:-1]}):\n{p.compoundStatement}'

    @_('')                                                               
    def emptyStatement(self, p):
        return f''

    @_('VAR IDENT ASSIGN expression')                                             
    def variableDeclaration(self, p):
        return f'\t'*p.VAR + f'{p.IDENT[:-1]} = {p.expression}'

    @_('FUNCTION IDENT LPAREN RPAREN compoundStatement')                          
    def functionDeclaration(self, p):     
        return f'\t'*p.FUNCTION + f'{p.IDENT[:-1]}():\n{p.compoundStatement}'

    @_('FUNCTION IDENT LPAREN args RPAREN compoundStatement')                    
    def functionDeclaration(self, p):     
        return f'\t'*p.FUNCTION + f'{p.IDENT[:-1]}({p.args}):\n{p.compoundStatement}'

    @_('IDENT COMMA args')
    def args(self, p):
        return f'{p.IDENT[:-1]}, {p.args}'

    @_('IDENT')
    def args(self, p):
        return f'{p.IDENT[:-1]}'

    @_('LPAREN expression RPAREN COMMA fargs')                                                         
    def fargs(self, p):                   
        return f'({p.expression}), {p.fargs}'
    
    @_('expression COMMA fargs')                                                         
    def fargs(self, p):                   
        return f'{p.expression}, {p.fargs}'
    
    @_('LPAREN expression RPAREN')                                                                   
    def fargs(self, p):                   
        return f'({p.expression})'
    
    @_('expression')                                                                   
    def fargs(self, p):                   
        return f'{p.expression}'
    
    @_('binop')                                                                   
    def expression(self, p):              
        return f'{p.binop}'

    @_('unop')                                                                    
    def binop(self, p):                   
        return f'{p.unop}'

    @_('binop ADD unop')                                                          
    def binop(self, p):                   
        return f'{p.binop} + {p.unop}'

    @_('binop SUB unop')                                                          
    def binop(self, p):                   
        return f'{p.binop} - {p.unop}'

    @_('binop MUL unop')                                                          
    def binop(self, p):                   
        return f'{p.binop} * {p.unop}'

    @_('binop DIV unop')                                                          
    def binop(self, p):                   
        return f'{p.binop} / {p.unop}'

    @_('binop MOD unop')                                                          
    def binop(self, p):                   
        return f'{p.binop} % {p.unop}'

    @_('binop LT unop')                                                           
    def binop(self, p):                   
        return f'{p.binop} < {p.unop}'

    @_('binop LTEQ unop')                                                         
    def binop(self, p):                   
        return f'{p.binop} <= {p.unop}'

    @_('binop GT unop')                                                           
    def binop(self, p):                   
        return f'{p.binop} > {p.unop}'

    @_('binop GTEQ unop')                                                         
    def binop(self, p):                   
        return f'{p.binop} >= {p.unop}'

    @_('binop EQ unop')                                                           
    def binop(self, p):                   
        return f'{p.binop} == {p.unop}'

    @_('binop NEQ unop')                                                          
    def binop(self, p):                   
        return f'{p.binop} != {p.unop}'

    @_('binop SAL unop')                                                          
    def binop(self, p):                   
        return f'{p.binop} << {p.unop}'

    @_('binop SAR unop')                                                          
    def binop(self, p):                   
        return f'{p.binop} >> {p.unop}'

    @_('binop BITAND unop')                                                       
    def binop(self, p):                   
        return f'{p.binop} & {p.unop}'

    @_('binop BITOR unop')                                                        
    def binop(self, p):                   
        return f'{p.binop} | {p.unop}'

    @_('binop BITXOR unop')                                                       
    def binop(self, p):                   
        return f'{p.binop} ^ {p.unop}'

    @_('binop AND unop')                                                          
    def binop(self, p):                   
        return f'{p.binop} and {p.unop}'

    @_('binop OR unop')                                                           
    def binop(self, p):                   
        return f'{p.binop} or {p.unop}'

    @_('term')                                                                    
    def unop(self, p):                    
        return f'{p.term}'

    @_('ADD term')                                                                
    def unop(self, p):                    
        return f'+{p.term}'

    @_('SUB term')                                                                
    def unop(self, p):                    
        return f'-{p.term}'

    @_('BITNOT term')                                                             
    def unop(self, p):                    
        return f'~{p.term}'

    @_('NOT term')                                                                
    def unop(self, p):                    
        return f'not {p.term}'

    @_('NUM')                                                                     
    def term(self, p):
        return f'{p.NUM}'

    @_('BOOL')                                                                    
    def term(self, p):
        if p.BOOL == 'true':                    
            return 'True'

        else:
            return 'False'

    @_('STRING')                                                                    
    def term(self, p):
        return f'{p.STRING}'

    @_('IDENT')                                                                    
    def term(self, p):
        return f'{p.IDENT[:-1]}'

    @_('LSQBR RSQBR')                                                       
    def term(self, p):
        return f'[]'

    @_('IDENT LSQBR expression RSQBR')                                                       
    def term(self, p):
        return f'{p.IDENT[:-1]}[{p.expression}]'

    @_('IDENT LSQBR expression SLICE expression RSQBR')                                                       
    def term(self, p):
        return f'{p.IDENT[:-1]}[{p.expression0} : {p.expression1}]'
    
    @_('LSQBR fargs RSQBR')                                                       
    def term(self, p):
        return f'[{p.fargs}]'

    @_('LPAREN expression RPAREN')                                                
    def term(self, p):
        return f'({p.expression})'


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