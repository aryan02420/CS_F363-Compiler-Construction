import sys
from sly import Parser
from .scanner import TetrisLexer


class TetrisParser(Parser):
    '''
program                 ::=   statements EOL                                                          { return f'{p.statements}\n'}

statements              ::=   statement                                                               { return f'{p.statement}'}
                        |     statement moreStatements                                                { return f'{p.statement}{p.moreStatements}'}

moreStatements          ::=   EOL statement                                                           { return f'\n{p.statement}' }
                        |     EOL moreStatements                                                      { return f'\n{p.moreStatements}' }

statement               ::=   assignmentStatement                                                     { return f'{p.assignmentStatement}' }
                        |     variableDeclaration                                                     { return f'{p.variableDeclaration}' }
                        |     functionStatement                                                       { return f'{p.functionStatement}' }
                        |     functionDeclaration                                                     { return f'{p.functionDeclaration}' }
                        |     compoundStatement                                                       { return f'{p.compoundStatement}' }
                        |     conditionalStatement                                                    { return f'{p.conditionalStatement}' }
                        |     loopStatement                                                           { return f'{p.loopStatement}' }
                        |     emptyStatement                                                          { return f'{p.emptyStatement}' }

assignmentStatement     ::=   IDENT ASSIGN expression                                                 { return f'{p.IDENT} = {p.expression}' }

functionStatement       ::=   IDENT LPAREN RPAREN                                                     { return f'{p.IDENT}()' }
                        |     IDENT LPAREN actparams RPAREN                                           { return f'{p.IDENT'({p.actparams}) }

actparams               ::=   expression                                                              { return f''{p.expression} }
                        |     expression moreparams                                                   { return f''{p.expression}{p.moreparams} }

moreparams              ::=   COMMA actparams                                                         { return f'', {p.actparams} }

compoundStatement       ::=   BEGIN statements END                                                    { return f''\n{p.statements}\n }

conditionalStatement    ::=   IF expression THEN statements                                           { return f'if {p.expression}:\n{p.statements}' }
                        |     IF expression THEN statements ELSE statements                           { return f'if {p.expression}:\n{p.statements0}\nelse:\n{p.statements1}' }

loopStatement           ::=   WHILE expression DO statement                                           { return f'while {p.expression}:\n\t{p.statement}' }
                        |     DO statement WHILE expression                                           { return f'{p.statement}\nwhile {p.expression}:\n\t{p.statement}' }
                        |     FOR IDENT ASSIGN NUM TO NUM DO statement                                { return f'for {p.IDENT} in range(p.NUM, p.NUM):\n\t{p.statement}'}

emptyStatement          ::=   /*empty*/                                                               { return f'' }

variableDeclaration     ::=   VAR IDENT ASSIGN expression                                             { return f'{p.IDENT} = {p.expression}' }

functionDeclaration     ::=   FUNCTION IDENT LPAREN RPAREN compoundStatement                          { return f'{p.IDENT}(){p.compoundStatement}' }
                        |     FUNCTION IDENT LPAREN fargs RPAREN compoundStatement                    { return f'{p.IDENT}({p.fargs}){p.compoundStatement}' }

fargs                   ::=   IDENT                                                                   { return f'{p.IDENT}'}
                        |     IDENT morefargs                                                         { return f'{p.IDENT}, {p.morefargs}' }

morefargs               ::=   COMMA fargs                                                             { return f', {p.fargs}' }

largs                   ::=   expression                                                              { return f'{p.expression}'}
                        |     expression morelargs                                                    { return f'{p.expression}, {p.morelargs}' }

morelargs               ::=   COMMA largs                                                             { return f', {p.largs}' }

expression              ::=   IDENT                                                                   { return f'{p.IDENT}' }
                        |     binop                                                                   { return f'{p.binop}' }
                        |     unop                                                                    { return f'{p.unop}' }

binop                   ::=   unop                                                                    { return f'{p.unop}' }
                        |     binop ADD unop                                                          { return f'{p.binop} + {p.unop}' }
                        |     binop SUB unop                                                          { return f'{p.binop} - {p.unop}' }
                        |     binop MUL unop                                                          { return f'{p.binop} * {p.unop}' }
                        |     binop DIV unop                                                          { return f'{p.binop} / {p.unop}' }
                        |     binop MOD unop                                                          { return f'{p.binop} % {p.unop}' }
                        |     binop LT unop                                                           { return f'{p.binop} < {p.unop}' }
                        |     binop LTEQ unop                                                         { return f'{p.binop} <= {p.unop}' }
                        |     binop GT unop                                                           { return f'{p.binop} > {p.unop}' }
                        |     binop GTEQ unop                                                         { return f'{p.binop} >= {p.unop}' }
                        |     binop EQ unop                                                           { return f'{p.binop} == {p.unop}' }
                        |     binop NEQ unop                                                          { return f'{p.binop} != {p.unop}' }
                        |     binop SAL unop                                                          { return f'{p.binop} << {p.unop}' }
                        |     binop SAR unop                                                          { return f'{p.binop} >> {p.unop}' }
                        |     binop BITAND unop                                                       { return f'{p.binop} & {p.unop}' }
                        |     binop BITOR unop                                                        { return f'{p.binop} | {p.unop}' }
                        |     binop BITXOR unop                                                       { return f'{p.binop} ^ {p.unop}' }
                        |     binop AND unop                                                          { return f'{p.binop} and {p.unop}' }
                        |     binop OR unop                                                           { return f'{p.binop} or {p.unop}' }

unop                    ::=   term                                                                    { return f'{p.term}' }
                        |     ADD term                                                                { return f'+{p.term}' }
                        |     SUB term                                                                { return f'-{p.term}' }
                        |     BITNOT term                                                             { return f'~{p.term}' }
                        |     NOT term                                                                { return f'not {p.term}' }

term                    ::=   NUM                                                                     { return f'{p.NUM}' }
                        |     BOOL                                                                    { return f'{p.BOOL}' }
                        |     STRING                                                                  { return f'{p.STRING}' }
                        |     LSQBR largs RSQBR                                                       { return f'[{p.largs}]' }
                        |     LPAREN expression RPAREN                                                { return f'({p.expression})' }
    '''
    tokens = TetrisLexer.tokens

    start = 'program'

    def __init__(self, tab_char, nesting_depth):
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

    ################changed##############
    @_('breakStatement')                                                       
    def semistatement(self, p):
        return f'{p.breakStatement}\n'

    @_('BREAK')                                                       
    def breakStatement(self, p):
        return f'{p.BREAK}\n'


    @_('continueStatement')                                                       
    def semistatement(self, p):
        return f'{p.continueStatement}\n'

    @_('CONTINUE')                                                       
    def continueStatement(self, p):
        return f'{p.CONTINUE}\n'
    #####################################

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

    ############changed#############
    @_('FLOAT')                                                                     
    def term(self, p):
        return f'{p.FLOAT}'
    ################################

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