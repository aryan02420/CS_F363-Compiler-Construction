# CS_F363-Compiler-Construction Project | BlockBusters

## Description:
<insert explanantion about the project>

## Installation and setup:
<insert options one can use, normal tetrislang package and also venv>

## Writing in tl and execution:
<insert instructions on how to run the code and get output>

## Demo:
<insert screenrecording and examples of running>

## Documentation:
<insert syntax explanation and docs for tl language>

## Future Plans after the project:


## Directory Structure:
<insert explanation of what folder is where>

```
.
├── Assignment
│   ├── assets
│   │   ├── 46786-50325-1-PB.pdf
│   │   ├── bb.png
│   │   ├── flowchart1.png
│   │   └── phases.jpeg
│   ├── bugs
│   │   └── bugs.txt
│   ├── compiler
│   │   ├── compiler.py
│   │   ├── output
│   │   │   ├── assets
│   │   │   │   ├── arcade.TTF
│   │   │   │   ├── highscore.txt
│   │   │   │   └── mario.ttf
│   │   │   ├── out1
│   │   │   ├── out2
│   │   │   ├── out3
│   │   │   └── tetris
│   │   ├── parser.out
│   │   ├── __pycache__
│   │   │   ├── parser.cpython-38.pyc
│   │   │   └── scanner.cpython-38.pyc
│   │   ├── sample_tlang_code
│   │   │   ├── case1.tl
│   │   │   ├── case2.tl
│   │   │   ├── case3.tl
│   │   │   └── tetris.tl
│   │   └── to_do.txt
│   ├── diagram
│   │   ├── diagram
│   │   │   ├── actparams.png
│   │   │   ├── addop.png
│   │   │   ├── assignmentStatement.png
│   │   │   ├── bitandop.png
│   │   │   ├── bitExpression.png
│   │   │   ├── bitxorop.png
│   │   │   ├── boolExpression.png
│   │   │   ├── cmpop.png
│   │   │   ├── comment.png
│   │   │   ├── compoundStatement.png
│   │   │   ├── conditionalStatement.png
│   │   │   ├── emptyStatement.png
│   │   │   ├── expression.png
│   │   │   ├── fargs.png
│   │   │   ├── functionDeclaration.png
│   │   │   ├── functionStatement.png
│   │   │   ├── loopStatement.png
│   │   │   ├── mulop.png
│   │   │   ├── program.png
│   │   │   ├── relationalExpression.png
│   │   │   ├── rr-1.63.png
│   │   │   ├── shiftop.png
│   │   │   ├── statement.png
│   │   │   ├── statements.png
│   │   │   ├── term.png
│   │   │   ├── unary.png
│   │   │   └── variableDeclaration.png
│   │   └── index.html
│   ├── engine
│   │   ├── assets
│   │   │   ├── arcade.TTF
│   │   │   ├── clear.wav
│   │   │   ├── gameover.wav
│   │   │   ├── highscore.txt
│   │   │   ├── key_press.wav
│   │   │   ├── mario.ttf
│   │   │   └── theme.wav
│   │   ├── __pycache__
│   │   │   └── tetris_engine.cpython-38.pyc
│   │   └── tetris_engine.py
│   ├── lex-diagram
│   │   ├── diagram
│   │   │   ├── AND.png
│   │   │   ├── ASSIGN.png
│   │   │   ├── BEGIN.png
│   │   │   ├── BOOL.png
│   │   │   ├── DO.png
│   │   │   ├── ELSE.png
│   │   │   ├── END.png
│   │   │   ├── EQ.png
│   │   │   ├── FOR.png
│   │   │   ├── FUNCTION.png
│   │   │   ├── GTEQ.png
│   │   │   ├── IDENT.png
│   │   │   ├── IF.png
│   │   │   ├── LTEQ.png
│   │   │   ├── NEQ.png
│   │   │   ├── NOT.png
│   │   │   ├── NUM.png
│   │   │   ├── OR.png
│   │   │   ├── Railroad-Diagram-Generator.png
│   │   │   ├── SAL.png
│   │   │   ├── SAR.png
│   │   │   ├── STRING.png
│   │   │   ├── THEN.png
│   │   │   ├── TO.png
│   │   │   ├── VAR.png
│   │   │   └── WHILE.png
│   │   └── index.html
│   ├── misc
│   │   ├── challenges.txt
│   │   ├── grammar.txt
│   │   ├── language-specs
│   │   ├── misc.txt
│   │   ├── new_grammar.txt
│   │   ├── scanner.txt
│   │   └── to_do.txt
│   ├── parser
│   │   └── tl_parser.py
│   ├── scanner
│   │   ├── midsem.sh
│   │   └── scanner.py
│   └── tests
│       ├── expected
│       │   ├── variable_assignment
│       │   └── variable_declaration
│       ├── input
│       │   ├── variable_assignment
│       │   └── variable_declaration
│       ├── output
│       │   ├── variable_assignment
│       │   └── variable_declaration
│       ├── runner.sh
│       └── tcompiler
├── EndSem Report - BlockBusters.pdf
├── MidSem Report - BlockBusters.pdf
├── README.md
├── requirements.txt
└── tetrislang
    ├── README.md
    ├── setup.py
    ├── tetrislang
    │   ├── assets
    │   │   ├── arcade.ttf
    │   │   ├── clear.wav
    │   │   ├── gameover.wav
    │   │   ├── highscore.txt
    │   │   ├── key_press.wav
    │   │   ├── mario.ttf
    │   │   └── theme.wav
    │   ├── bin
    │   │   └── tetris-lang
    │   ├── compiler.py
    │   ├── engine.py
    │   ├── __init__.py
    │   ├── parser.py
    │   ├── __pycache__
    │   │   ├── compiler.cpython-38.pyc
    │   │   ├── engine.cpython-38.pyc
    │   │   ├── __init__.cpython-38.pyc
    │   │   ├── parser.cpython-38.pyc
    │   │   └── scanner.cpython-38.pyc
    │   └── scanner.py
    └── tetrislang.egg-info
        ├── dependency_links.txt
        ├── not-zip-safe
        ├── PKG-INFO
        ├── requires.txt
        ├── SOURCES.txt
        └── top_level.txt

28 directories, 133 files
```
