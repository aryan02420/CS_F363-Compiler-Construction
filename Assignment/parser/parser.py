from sly import Parser
import sys
sys.path.append("..")
from scanner.scanner import CalcLexer


class CalcParser(Parser):
    debugfile = 'parser.out'
    # Get the token list from the lexer (required)
    tokens = CalcLexer.tokens

    start = 'program'

    @_('statements EOL')                                                          
    def program(self, p):                 
        return f'{p.statements}\n'

    @_('statement')                                                               
    def statements(self, p):              
        return f'{p.statement}'

    @_('statement moreStatements')                                                
    def statements(self, p):              
        return f'{p.statement}{p.moreStatements}'

    @_('EOL statement')                                                           
    def moreStatements(self, p):          
        return f'\n{p.statement}'

    @_('EOL moreStatements')                                                      
    def moreStatements(self, p):          
        return f'\n{p.moreStatements}'

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

    @_('functionDeclaration')                                                     
    def statement(self, p):               
        return f'{p.functionDeclaration}'

    @_('compoundStatement')                                                       
    def statement(self, p):               
        return f'{p.compoundStatement}'

    @_('conditionalStatement')                                                    
    def statement(self, p):               
        return f'{p.conditionalStatement}'

    @_('loopStatement')                                                           
    def statement(self, p):               
        return f'{p.loopStatement}'


    @_('IDENT ASSIGN expression')                                                 
    def assignmentStatement(self, p):     
        return f'{p.IDENT} = {p.expression}'

    @_('IDENT LPAREN RPAREN')                                                     
    def functionStatement(self, p):       
        return f'{p.IDENT}()'

    @_('IDENT LPAREN actparams RPAREN')                                           
    def functionStatement(self, p):       
        return f'{p.IDENT}({p.actparams})'

    @_('expression')                                                              
    def actparams(self, p):               
        return f'{p.expression}'

    @_('expression moreparams')                                                   
    def actparams(self, p):               
        return f'{p.expression}{p.moreparams}'

    @_('COMMA actparams')                                                         
    def moreparams(self, p):              
        return f', {p.actparams}'

    @_('BEGIN statements END')                                                    
    def compoundStatement(self, p):       
        return f'\n{p.statements}\n'

    @_('IF expression THEN statements')                                           
    def conditionalStatement(self, p):    
        return f'if {p.expression}:\n{p.statements}'

    @_('IF expression THEN statements ELSE statements')                           
    def conditionalStatement(self, p):    
        return f'if {p.expression}:\n{p.statements0}\nelse:\n{p.statements1}'

    @_('WHILE expression DO statement')                                           
    def loopStatement(self, p):           
        return f'while {p.expression}:\n\t{p.statement}'

    @_('DO statement WHILE expression')                                           
    def loopStatement(self, p):           
        return f'{p.statement}\nwhile {p.expression}:\n\t{p.statement}'

    @_('FOR IDENT ASSIGN NUM TO NUM DO statement')                          
    def loopStatement(self, p):           
        return f'for {p.IDENT} in range(p.NUM, p.NUM):\n\t{p.statement}'

    @_('')                                                               
    def emptyStatement(self, p):          
        return f''

    @_('VAR IDENT ASSIGN expression')                                             
    def variableDeclaration(self, p):     
        return f'{p.IDENT} = {p.expression}'

    @_('FUNCTION IDENT LPAREN RPAREN compoundStatement')                          
    def functionDeclaration(self, p):     
        return f'{p.IDENT}(){p.compoundStatement}'

    @_('FUNCTION IDENT LPAREN fargs RPAREN compoundStatement')                    
    def functionDeclaration(self, p):     
        return f'{p.IDENT}({p.fargs}){p.compoundStatement}'

    @_('IDENT')                                                                   
    def fargs(self, p):                   
        return f'{p.IDENT}'

    @_('IDENT morefargs')                                                         
    def fargs(self, p):                   
        return f'{p.IDENT}, {p.morefargs}'

    @_('COMMA fargs')                                                             
    def morefargs(self, p):               
        return f', {p.fargs}'

    @_('expression')                                                              
    def largs(self, p):                   
        return f'{p.expression}'

    @_('expression morelargs')                                                    
    def largs(self, p):                   
        return f'{p.expression}, {p.morelargs}'

    @_('COMMA largs')                                                             
    def morelargs(self, p):               
        return f', {p.largs}'

    @_('IDENT')                                                                   
    def expression(self, p):              
        return f'{p.IDENT}'

    @_('binop')                                                                   
    def expression(self, p):              
        return f'{p.binop}'

    @_('unop')                                                                    
    def expression(self, p):              
        return f'{p.unop}'

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
        return f'{p.BOOL}'

    @_('STRING')                                                                    
    def term(self, p):                    
        return f'{p.STRING}'

    @_('LSQBR largs RSQBR')                                                       
    def term(self, p):                    
        return f'[{p.largs}]'

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