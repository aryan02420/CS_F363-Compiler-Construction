import sys
from scanner.scanner import CalcLexer
from parser.parser import CalcParser

if __name__ == '__main__':
    lexer = CalcLexer()
    parser = CalcParser()

    input_code = ""
    with open(sys.argv[1], 'r') as f:
        input_code = f.read()

    print("INPUT")
    # print(input_code)

    tokens = lexer.tokenize(input_code)

    print("TOKENS")
    # print('\n'.join([f'{tok.type}\t{tok.value}' for tok in tokens]))

    output = parser.parse(lexer.tokenize(input_code))
    
    print("OUTPUT")
    print(output)

    with open(sys.argv[2], 'w') as f:
        f.write(output)



# if __name__ == '__main__':
#     lexer = CalcLexer()
#     parser = CalcParser()

#     while True:
#         try:
#             text = input('calc > ')
#             print(text)
#             result = parser.parse(lexer.tokenize(text))
#             print(result)
#         except EOFError:
#             break