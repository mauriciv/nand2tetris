#! /usr/bin/python3
from parser import Parser
import code
from symbol_table import SymbolTable
import sys
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print('Error. No .asm file provided.')
        exit(1)
    program_name = Path(sys.argv[1]).name
    symbol_table = generate_symbols(sys.argv[1])
    code = compile(sys.argv[1], symbol_table)
    with open(program_name.split('.')[0] + '.hack', 'x') as target:
        target.write(code)

def generate_symbols(file):
    symbol_table = SymbolTable()
    instruction_number = 0
    with open(file) as f:
        parser = Parser(f)
        while parser.has_more_commands():
            if parser.command_type() is 'L_COMMAND' and not symbol_table.contains(parser.symbol()):
                symbol_table.add_entry(parser.symbol(), instruction_number)
            if parser.command_type() is 'A_COMMAND' or parser.command_type() is 'C_COMMAND':
                instruction_number += 1
                # line = decoder.bin(p.symbol()) + '\n'
            parser.advance()
    return symbol_table


def compile(file, symbol_table):
    with open(file) as f:
        parser = Parser(f)
        decoder = code.Code()
        binary = ''
        free_ram_address = 16
        while parser.has_more_commands():
            line = ''
            if parser.command_type() is 'A_COMMAND':
                try:
                    line = decoder.bin(int(parser.symbol())) + '\n'
                except ValueError:
                    if symbol_table.contains(parser.symbol()):
                        decimal_address = symbol_table.get_address(parser.symbol())
                        line = decoder.bin(decimal_address) + '\n'
                    else:
                        symbol_table.add_entry(parser.symbol(), free_ram_address)
                        line = decoder.bin(free_ram_address) + '\n'
                        free_ram_address += 1

            elif parser.command_type() is 'C_COMMAND':
                line = '111' + decoder.comp(parser.comp()) + decoder.dest(parser.dest()) + decoder.jump(parser.jump()) + '\n'
            else:
                print('L_COMMAND')
            binary += line
            parser.advance()
        return binary.strip()

if __name__ == '__main__':
    main()