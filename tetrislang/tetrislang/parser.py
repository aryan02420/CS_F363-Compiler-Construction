import sys
from sly import Parser
from .scanner import TetrisLexer

class SlyLogger(object):
    def __init__(self, f):
        self.f = f

    def debug(self, msg, *args, **kwargs):
        self.f.write((msg % args) + '\n')

    info = debug

    def warning(self, msg, *args, **kwargs):
        return

    def error(self, msg, *args, **kwargs):
        self.f.write('ERROR: ' + (msg % args) + '\n')

    critical = debug

class YaccSymbol:
    def __str__(self):
        return self.type

    def __repr__(self):
        return str(self)

class YaccProduction:
    __slots__ = ('_slice', '_namemap', '_stack')
    def __init__(self, s, stack=None):
        self._slice = s
        self._namemap = { }
        self._stack = stack

    def __getitem__(self, n):
        if n >= 0:
            return self._slice[n].value
        else:
            return self._stack[n].value

    def __setitem__(self, n, v):
        if n >= 0:
            self._slice[n].value = v
        else:
            self._stack[n].value = v

    def __len__(self):
        return len(self._slice)

    @property
    def lineno(self):
        for tok in self._slice:
            if isinstance(tok, YaccSymbol):
                continue
            lineno = getattr(tok, 'lineno', None)
            if lineno:
                return lineno
        raise AttributeError('No line number found')

    @property
    def index(self):
        for tok in self._slice:
            if isinstance(tok, YaccSymbol):
                continue
            index = getattr(tok, 'index', None)
            if index is not None:
                return index
        raise AttributeError('No index attribute found')

    def __getattr__(self, name):
        if name in self._namemap:
            return self._namemap[name](self._slice)
        else:
            nameset = '{' + ', '.join(self._namemap) + '}'
            raise AttributeError(f'No symbol {name}. Must be one of {nameset}.')

    def __setattr__(self, name, value):
        if name[:1] == '_':
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"Can't reassign the value of attribute {name!r}")

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

    ERROR_COUNT = 3                # Number of symbols that must be shifted to leave recovery mod
    log = SlyLogger(sys.stderr)
    
    tokens = TetrisLexer.tokens
    err = False
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

    @_('')
    def errorToken(self, p):
        pass

    # error

    def error(self, p):
        print(f"Syntax error at Line: {p.lineno} Index: {p.index}, token {p.type} '{p.value}'")
        self.err = True

    @_('IF errorToken expression')
    def conditionalStatement(self, p):
        print(f"Syntax Error at Line: {p.lineno}. expected '(' before '{p.expression}'")
        self.err = True

    @_('WHILE errorToken expression')
    def loopStatement(self, p):
        print(f"Syntax Error at Line: {p.lineno}. expected '(' before '{p.expression}'")
        self.err = True

    @_('FOR errorToken IDENT')
    def loopStatement(self, p):
        print(f"Syntax Error at Line: {p.lineno}. expected '(' before '{p.expression}'")
        self.err = True
    
    @_('semistatement errorToken statements')
    def statements(self, p):
        print(f"Syntax Error in Line. expected ';' after '{p.semistatement.strip()}'")
        self.err = True

    @_('VAR IDENT errorToken expression')
    def variableDeclaration(self, p):
        print(f"Syntax Error at Line: {p.lineno}. expected ':=' before '{p.expression}'")
        self.err = True

    @_('IDENT errorToken expression')
    def assignmentStatement(self, p):
        print(f"Syntax Error at Line: {p.lineno}. expected ':=' before '{p.expression}'")
        self.err = True

    @_('IDENT LSQBR expression RSQBR errorToken expression')   
    def assignmentStatement(self, p):
        print(f"Syntax Error at Line: {p.lineno}. expected ':=' before '{p.expression}'")
        self.err = True

    def parse(self, tokens):
        '''
        Parse the given input tokens.
        '''
        lookahead = None                                  # Current lookahead symbol
        lookaheadstack = []                               # Stack of lookahead symbols
        actions = self._lrtable.lr_action                 # Local reference to action table (to avoid lookup on self.)
        goto    = self._lrtable.lr_goto                   # Local reference to goto table (to avoid lookup on self.)
        prod    = self._grammar.Productions               # Local reference to production list (to avoid lookup on self.)
        defaulted_states = self._lrtable.defaulted_states # Local reference to defaulted states
        pslice  = YaccProduction(None)                    # Production object passed to grammar rules
        errorcount = 0                                    # Used during error recovery

        # Set up the state and symbol stacks
        self.tokens = tokens
        self.statestack = statestack = []                 # Stack of parsing states
        self.symstack = symstack = []                     # Stack of grammar symbols
        pslice._stack = symstack                           # Associate the stack with the production
        self.restart()

        errtoken   = None                                 # Err token
        while True:
            # Get the next symbol on the input.  If a lookahead symbol
            # is already set, we just use that. Otherwise, we'll pull
            # the next token off of the lookaheadstack or from the lexer
            if self.state not in defaulted_states:
                if not lookahead:
                    if not lookaheadstack:
                        lookahead = next(tokens, None)  # Get the next token
                    else:
                        lookahead = lookaheadstack.pop()
                    if not lookahead:
                        lookahead = YaccSymbol()
                        lookahead.type = '$end'

                # Check the action table
                ltype = lookahead.type
                t = actions[self.state].get(ltype)
            else:
                t = defaulted_states[self.state]

            if t is not None:
                if t > 0:
                    # shift a symbol on the stack
                    statestack.append(t)
                    self.state = t

                    symstack.append(lookahead)
                    lookahead = None

                    # Decrease error count on successful shift
                    if errorcount:
                        errorcount -= 1
                    continue

                if t < 0:
                    # reduce a symbol on the stack, emit a production
                    self.production = p = prod[-t]
                    pname = p.name
                    plen  = p.len
                    pslice._namemap = p.namemap

                    # Call the production function
                    pslice._slice = symstack[-plen:] if plen else []

                    sym = YaccSymbol()
                    sym.type = pname       
                    value = p.func(self, pslice)
                    if value is pslice:
                        value = (pname, *(s.value for s in pslice._slice))
                    sym.value = value
                    if plen:
                        del symstack[-plen:]
                        del statestack[-plen:]

                    symstack.append(sym)
                    self.state = goto[statestack[-1]][pname]
                    statestack.append(self.state)
                    continue

                if t == 0:
                    n = symstack[-1]
                    result = getattr(n, 'value', None)
                    return self.err, result

            if t is None:
                # We have some kind of parsing error here.  To handle
                # this, we are going to push the current token onto
                # the tokenstack and replace it with an 'error' token.
                # If there are any synchronization rules, they may
                # catch it.
                #
                # In addition to pushing the error token, we call call
                # the user defined error() function if this is the
                # first syntax error.  This function is only called if
                # errorcount == 0.
                if errorcount == 0 or self.errorok:
                    errorcount = self.ERROR_COUNT
                    self.errorok = False
                    if lookahead.type == '$end':
                        errtoken = None               # End of file!
                    else:
                        errtoken = lookahead

                    tok = self.error(errtoken)
                    if tok:
                        # User must have done some kind of panic
                        # mode recovery on their own.  The
                        # returned token is the next lookahead
                        lookahead = tok
                        self.errorok = True
                        continue
                    else:
                        # If at EOF. We just return. Basically dead.
                        if not errtoken:
                            return
                else:
                    # Reset the error count.  Unsuccessful token shifted
                    errorcount = self.ERROR_COUNT

                # case 1:  the statestack only has 1 entry on it.  If we're in this state, the
                # entire parse has been rolled back and we're completely hosed.   The token is
                # discarded and we just keep going.

                if len(statestack) <= 1 and lookahead.type != '$end':
                    lookahead = None
                    self.state = 0
                    # Nuke the lookahead stack
                    del lookaheadstack[:]
                    continue

                # case 2: the statestack has a couple of entries on it, but we're
                # at the end of the file. nuke the top entry and generate an error token

                # Start nuking entries on the stack
                if lookahead.type == '$end':
                    # Whoa. We're really hosed here. Bail out
                    return

                if lookahead.type != 'error':
                    sym = symstack[-1]
                    if sym.type == 'error':
                        # Hmmm. Error is on top of stack, we'll just nuke input
                        # symbol and continue
                        lookahead = None
                        continue

                    # Create the error symbol for the first time and make it the new lookahead symbol
                    t = YaccSymbol()
                    t.type = 'error'

                    if hasattr(lookahead, 'lineno'):
                        t.lineno = lookahead.lineno
                    if hasattr(lookahead, 'index'):
                        t.index = lookahead.index
                    t.value = lookahead
                    lookaheadstack.append(lookahead)
                    lookahead = t
                else:
                    sym = symstack.pop()
                    statestack.pop()
                    self.state = statestack[-1]
                continue

            # Call an error function here
            raise RuntimeError('sly: internal parser error!!!\n')



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