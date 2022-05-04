import sys
import re
import argparse

from .scanner import TetrisLexer
from .parser import TetrisParser

def TetrisCompiler(code, debug=False):
    lexer = TetrisLexer()
    parser = TetrisParser('    ', '1')

    # comment shebang
    code = re.sub(r'^(#![^\r\n]+)', r'// \1', code)

    header = \
'''#!/usr/bin/env python3

import sys
from tetrislang import TetrisEngine

engine = TetrisEngine()

def Game():
'''

    footer = \
'''
if __name__ == '__main__':
    Game()
'''

    flag, generated = parser.parse(lexer.tokenize(code))

    if flag == True:
        raise Exception("Above Syntax Errors were encountered while parsing the input!")
    
    output = '\n'.join([header, generated, footer])

    if (debug):
        tokens = lexer.tokenize(code)
        print("TOKENS")
        print('\n'.join([f'{tok.type}\t{tok.value}' for tok in tokens]))
        print("OUPUT")
        print(output)

    return output


if __name__ == '__main__':

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True, help="path to the tlang (.tl) code to be compiled")
    ap.add_argument("-o", "--output", required=True, help="path to the output python (.py) code that will be generated post compilation")
    ap.add_argument("-d", "--debug", required=False, default=False, action=argparse.BooleanOptionalAction, help="Show additional output")
    args = vars(ap.parse_args())

    input_code = ""

    if args.get("input", False):
        input_path = args["input"]

    if args.get("output", False):
        output_path = args["output"]

    with open(input_path, 'r') as f:
        input_code = f.read()

    with open(output_path, 'w') as f:
        output = TetrisCompiler(input_code, args["debug"])
        f.write(output)

    print(f"Compilation Successful!\nOutput file generated at: {output_path}\nRun the output file to launch the game.")