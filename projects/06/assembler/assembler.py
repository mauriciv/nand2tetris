#! /usr/bin/python3
import parser
import code
import sys
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print('Error. No .asm file provided.')
        exit(1)
    program_name = Path(sys.argv[1]).name
    code = compile(sys.argv[1])
    with open(program_name.split('.')[0] + '.hack', 'x') as target:
        target.write(code)

def compile(file):
    with open(file) as f:
        p = parser.Parser(f)
        decoder = code.Code()
        binary = ''
        while p.has_more_commands():
            line = ''
            if p.command_type() is 'A_COMMAND' or p.command_type() is 'L_COMMAND':
                line = decoder.bin(p.symbol()) + '\n'
                pass
            elif p.command_type() is 'C_COMMAND':
                line = '111' + decoder.comp(p.comp()) + decoder.dest(p.dest())   + decoder.jump(p.jump()) + '\n'
            else:
                print('Unrecognized command')
            binary += line
            p.advance()
        return binary.strip()

if __name__ == '__main__':
    main()