import sys
from pathlib import Path
from parser import Parser

def main():
    if len(sys.argv) < 2:
        print('Error. No .vm file provided.')
        exit(1)
    program_name = Path(sys.argv[1]).name
    with open(sys.argv[1]) as f:
        parser = Parser(f)
        while parser.has_more_commands():
            # print(parser.command_type())
            print(parser.arg1() + ' ' + parser.arg2())
            parser.advance()
    # symbol_table = generate_symbols(sys.argv[1])
    # code = compile(sys.argv[1], symbol_table)
    # with open(program_name.split('.')[0] + '.hack', 'x') as target:
    #     target.write(code)

if __name__ == "__main__":
    main()