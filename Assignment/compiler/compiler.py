import sys
import argparse
sys.path.append(sys.path[0][:(sys.path[0].find('Assignment/')) + len('Assignment/')] + 'scanner')
sys.path.append(sys.path[0][:(sys.path[0].find('Assignment/')) + len('Assignment/')] + 'parser')

from scanner import CalcLexer
from tl_parser import CalcParser

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", help="path to the tlang (.tl) code to be compiled")
ap.add_argument("-o", "--output",help="path to the output python (.py) code that will be generated post compilation")
args = vars(ap.parse_args())

if __name__ == '__main__':
    lexer = CalcLexer()
    parser = CalcParser()

    input_code = ""

    if args.get("input", False):
        input_path = args["input"]

    if args.get("output", False):
        output_path = args["output"]

    with open(input_path, 'r') as f:
        input_code = f.read()

    # print("INPUT")
    # print(input_code)

    # tokens = lexer.tokenize(input_code)

    # print("TOKENS")
    # print('\n'.join([f'{tok.type}\t{tok.value}' for tok in tokens]))

    header = '''
    #!/usr/bin/python3
    import sys
    sys.path.append(sys.path[0][:(sys.path[0].find('Assignment/')) + len('Assignment/')] + 'engine')\n
    from tetris_engine import TetrisEngine\n
    engine = TetrisEngine()\n
    '''
    output = parser.parse(lexer.tokenize(input_code))
    
    with open(output_path, 'w') as f:
        f.write(header)
        f.write(output)
    
    
    if output != None:
        print(f"Compilation Successful!\nOutput file generated at: {output_path}\nRun the output file to launch the game.")
        # print("OUTPUT")
        # print(output)
    else:
        print(f"Compilation NOT Successful! :(\n")