import sys
from sly import Parser
from .scanner import TetrisLexer


class TetrisParser(Parser):
    '''
program                 ::=     functionDeclarations statements

statements              ::=     semistatement EOL statements                                                              
                        |       nosemistatement statements
                        |       emptyStatement

semistatement           ::=     emptyStatement                                                     
                        |       variableDeclaration                                                        
                        |       assignmentStatement  
                        |       functionStatement
                        |       breakStatement
                        |       continueStatement

nosemistatement         ::=     compoundStatement
                        |       conditionalStatement
                        |       loopStatement                                               

emptyStatement          ::=     /*empty*/    

variableDeclaration     ::=     VAR IDENT ASSIGN expression

assignmentStatement     ::=     IDENT ASSIGN expression
                        |       IDENT LSQBR expression RSQBR ASSIGN expression                                                

functionStatement       ::=     IDENT LPAREN RPAREN                                                     
                        |       IDENT LPAREN args RPAREN                                                                  

compoundStatement       ::=     BEGIN statements END

functionDeclarations    ::=     functionDeclaration functionDeclarations
                        |       emptyStatement

functionDeclaration     ::=     FUNCTION IDENT LPAREN RPAREN _indent compoundStatement _outdent
                        |       FUNCTION IDENT LPAREN params RPAREN _indent compoundStatement _outdent

condition               ::=     LPAREN expression RPAREN

conditionalStatement    ::=     IF condition _indent compoundStatement _outdent
                        |       IF condition _indent compoundStatement _outdent ELSE _indent compoundStatement _outdent

loopStatement           ::=     WHILE condition _indent compoundStatement _outdent
                        |       FOR LPAREN IDENT ASSIGN expression TO expression RPAREN _indent compoundStatement _outdent                                          

params                  ::=     IDENT COMMA params                                                               
                        |       IDENT

args                    ::=     expression COMMA args
                        |       expression

expression              ::=     binop                                                                   

binop                   ::=     unop                                                                   
                        |       binop ADD unop                                                         
                        |       binop SUB unop                                                         
                        |       binop MUL unop                                                         
                        |       binop DIV unop                                                         
                        |       binop MOD unop                                                         
                        |       binop LT unop                                                          
                        |       binop LTEQ unop                                                        
                        |       binop GT unop                                                          
                        |       binop GTEQ unop                                                        
                        |       binop EQ unop                                                          
                        |       binop NEQ unop                                                         
                        |       binop SAL unop                                                         
                        |       binop SAR unop                                                         
                        |       binop BITAND unop                                                       
                        |       binop BITOR unop                                                       
                        |       binop BITXOR unop                                                       
                        |       binop AND unop                                                         
                        |       binop OR unop      

unop                    ::=     term
                        |       ADD term
                        |       SUB term
                        |       BITNOT term
                        |       NOT term

list                    ::=     LSQBR args RSQBR

term                    ::=     NUM
                        |       FLOAT
                        |       BOOL
                        |       STRING
                        |       IDENT
                        |       list
                        |       functionStatement
                        |       LPAREN expression RPAREN
                        |       IDENT LSQBR expression RSQBR
    '''
    tokens = TetrisLexer.tokens

    start = 'program'

    def __init__(self, tab_char='\t', nesting_depth=0):
        self.tab_char = tab_char
        self.nesting_depth = int(nesting_depth)

    # program

    @_('functionDeclarations statements')                                                          
    def program(self, p):
        return f'{p.functionDeclarations}{p.statements}'

    # statements 

    @_('semistatement EOL statements')                                                
    def statements(self, p):
        return f'{self.tab_char*self.nesting_depth}{p.semistatement}{p.statements}'

    @_('nosemistatement statements')                                                               
    def statements(self, p):
        return f'\n{self.tab_char*self.nesting_depth}{p.nosemistatement}\n{p.statements}'

    @_('emptyStatement')                                                               
    def statements(self, p):
        return f'{p.emptyStatement}'

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

    @_('breakStatement')                                                       
    def semistatement(self, p):
        return f'{p.breakStatement}\n'

    @_('continueStatement')                                                       
    def semistatement(self, p):
        return f'{p.continueStatement}\n'

    # no semi statement 

    @_('compoundStatement')                                                       
    def nosemistatement(self, p):
        return f'{p.compoundStatement}'

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

    # function defs

    @_('functionDeclaration functionDeclarations')                                                               
    def functionDeclarations(self, p):
        return f'{self.tab_char*self.nesting_depth}{p.functionDeclaration}{p.functionDeclarations}'

    @_('emptyStatement')                                                               
    def functionDeclarations(self, p):
        return f'{p.emptyStatement}'

    # function def

    @_('FUNCTION IDENT LPAREN RPAREN indent compoundStatement outdent')                          
    def functionDeclaration(self, p):     
        return f'def {p.IDENT}():\n{p.compoundStatement}'

    @_('FUNCTION IDENT LPAREN params RPAREN indent compoundStatement outdent')                    
    def functionDeclaration(self, p):     
        return f'def {p.IDENT}({p.params}):\n{p.compoundStatement}'

    # condition

    @_('LPAREN expression RPAREN')                                           
    def condition(self, p):
        return f'{p.expression}'

    # conditionals

    @_('IF condition indent compoundStatement outdent')                                           
    def conditionalStatement(self, p):
        return f'if {p.condition}:\n{p.compoundStatement}'

    @_('IF condition indent compoundStatement outdent ELSE indent compoundStatement outdent')                           
    def conditionalStatement(self, p):
        return f'if {p.condition}:\n{p.compoundStatement0}{self.tab_char*self.nesting_depth}else:\n{p.compoundStatement1}'
    
    # loops

    @_('WHILE condition indent compoundStatement outdent')                                           
    def loopStatement(self, p):           
        return f'while {p.condition}:\n{p.compoundStatement}'

    @_('FOR LPAREN IDENT ASSIGN expression TO expression RPAREN indent compoundStatement outdent')                          
    def loopStatement(self, p):           
        return f'for {p.IDENT} in range({p.expression0}, {p.expression1}):\n{p.compoundStatement}'

    # loop control

    @_('BREAK')                                                       
    def breakStatement(self, p):
        return f'{p.BREAK}'

    @_('CONTINUE')                                                       
    def continueStatement(self, p):
        return f'{p.CONTINUE}'

    # params and args

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
    
    @_('LSQBR args RSQBR')                                                                     
    def list(self, p):
        return f'[{p.args}]'
    
    # terms

    @_('NUM')                                                                     
    def term(self, p):
        return f'{p.NUM}'

    @_('FLOAT')                                                                     
    def term(self, p):
        return f'{p.FLOAT}'

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

    # error

    def error(self, p):
        print(f"Syntax error at Line: {p.lineno}, token {p.type} '{p.value}'")


if __name__ == '__main__':
    lexer = TetrisLexer()
    parser = TetrisParser()

    while True:
        try:
            text = input('>> ')
            result = parser.parse(lexer.tokenize(text))
            print(result)
        except Exception as e:
            print(e)