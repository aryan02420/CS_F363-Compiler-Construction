import sys
sys.path.append(sys.path[0][:(sys.path[0].find('Assignment/')) + len('Assignment/')] + 'scanner')

from sly import Parser
from scanner import CalcLexer


class CalcParser(Parser):
    # debugfile = 'parser.out'
    tokens = CalcLexer.tokens

    start = 'program'

    def __init__(self):
        self.tabChar = '    '
        self.nesting_depth = 0

    # program

    @_('statements')                                                          
    def program(self, p):
        return f'{p.statements}'

    # statements 

    @_('semistatement EOL statements')                                                
    def statements(self, p):
        return f'{self.tabChar*self.nesting_depth}{p.semistatement}{p.statements}'

    @_('nosemistatement statements')                                                               
    def statements(self, p):
        return f'{self.tabChar*self.nesting_depth}{p.nosemistatement}\n{p.statements}'

    @_('emptyStatement')                                                               
    def statements(self, p):
        return f'{self.tabChar*self.nesting_depth}{p.emptyStatement}'

    # semi statement

    @_('emptyStatement')                                                          
    def semistatement(self, p):
        return f'{p.emptyStatement}'

    @_('variableDeclaration')                                                     
    def semistatement(self, p):
        return f'{p.variableDeclaration}\n'

    @_('assignmentStatement')                                                     
    def semistatement(self, p):
        return f'{p.assignmentStatement}\n'

    @_('functionStatement')                                                       
    def semistatement(self, p):
        return f'{p.functionStatement}\n'

    # no semi statement 

    @_('emptyStatement')                                                       
    def nosemistatement(self, p):
        return f'{p.emptyStatement}'

    @_('compoundStatement')                                                       
    def nosemistatement(self, p):
        return f'{p.compoundStatement}'

    @_('functionDeclaration')                                                       
    def nosemistatement(self, p):
        return f'{p.functionDeclaration}'

    @_('conditionalStatement')                                                    
    def nosemistatement(self, p):
        return f'{p.conditionalStatement}'

    @_('loopStatement')                                                           
    def nosemistatement(self, p):               
        return f'{p.loopStatement}'

    # empty statement 

    @_('')                                                               
    def emptyStatement(self, p):
        return ''

    # var declaration

    @_('VAR IDENT ASSIGN expression')                                             
    def variableDeclaration(self, p):
        return f'{p.IDENT} = {p.expression}'

    # assignment

    @_('IDENT ASSIGN expression')                                                 
    def assignmentStatement(self, p):
        return f'{p.IDENT} = {p.expression}'

    @_('IDENT LSQBR expression RSQBR ASSIGN expression')                                                 
    def assignmentStatement(self, p):
        return f'{p.IDENT}[{p.expression0}] = {p.expression1}'

    # function call

    @_('IDENT LPAREN RPAREN')                                                     
    def functionStatement(self, p):
        return f'{p.IDENT}()'

    @_('IDENT LPAREN args RPAREN')                                           
    def functionStatement(self, p):
        return f'{p.IDENT}({p.args})'

    # compound

    @_('BEGIN statements END')                                                    
    def compoundStatement(self, p):
        return f'{p.statements}'

    # function def

    @_('FUNCTION IDENT LPAREN RPAREN indent compoundStatement outdent')                          
    def functionDeclaration(self, p):     
        return f'def {p.IDENT}():\n{p.compoundStatement}'

    @_('FUNCTION IDENT LPAREN params RPAREN indent compoundStatement outdent')                    
    def functionDeclaration(self, p):     
        return f'def {p.IDENT}({p.params}):\n{p.compoundStatement}'

    # conditionals

    @_('IF LPAREN expression RPAREN indent compoundStatement outdent')                                           
    def conditionalStatement(self, p):
        return f'if {p.expression}:\n{p.compoundStatement}'

    @_('IF LPAREN expression RPAREN indent compoundStatement outdent ELSE indent compoundStatement outdent')                           
    def conditionalStatement(self, p):
        return f'if {p.expression}:\n{p.compoundStatement0}else:{p.compoundStatement1}'
    
    # loops

    @_('WHILE LPAREN expression RPAREN indent compoundStatement outdent')                                           
    def loopStatement(self, p):           
        return f'while {p.expression}:\n{p.compoundStatement}'

    @_('FOR LPAREN IDENT ASSIGN expression TO expression RPAREN indent compoundStatement outdent')                          
    def loopStatement(self, p):           
        return f'for {p.IDENT} in range({p.expression0}, {p.expression1}):\n{p.compoundStatement}'


    # lists

    @_('IDENT COMMA params')
    def params(self, p):
        return f'{p.IDENT}, {p.params}'

    @_('IDENT')
    def params(self, p):
        return f'{p.IDENT}'
    
    @_('expression COMMA args')                                                         
    def args(self, p):                   
        return f'{p.expression}, {p.args}'
    
    @_('expression')                                                                   
    def args(self, p):                   
        return f'{p.expression}'

    # expression
    
    @_('binop')                                                                   
    def expression(self, p):              
        return f'{p.binop}'
    
    # binary operations

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

    # uniary operations

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

    # list type
    
    @_('LSQBR RSQBR')                                                                     
    def list(self, p):
        return f'[]'
    
    @_('LSQBR args RSQBR')                                                                     
    def list(self, p):
        return f'[{p.args}]'
    
    # terms

    @_('NUM')                                                                     
    def term(self, p):
        return f'{p.NUM}'

    @_('BOOL')                                                                    
    def term(self, p):
        if p.BOOL == 'true':                    
            return 'True'
        return 'False'

    @_('STRING')                                                                    
    def term(self, p):
        return f'{p.STRING}'

    @_('IDENT')                                                                    
    def term(self, p):
        return f'{p.IDENT}'

    @_('list')                                                       
    def term(self, p):
        return f'{p.list}'

    @_('functionStatement')                                                
    def term(self, p):
        return f'{p.functionStatement}'

    @_('LPAREN expression RPAREN')                                                       
    def term(self, p):
        return f'({p.expression})'  

    @_('IDENT LSQBR expression RSQBR')                                                       
    def term(self, p):
        return f'{p.IDENT}[{p.expression}]'  

    # helpers

    @_('')                                                
    def indent(self, p):
        self.nesting_depth += 1

    @_('')                                                
    def outdent(self, p):
        self.nesting_depth -= 1


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
