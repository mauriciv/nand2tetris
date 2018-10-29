class Parser():

    def __init__(self, file):
        content = [line.strip() for line in file.readlines()]
        content = [line.split('//')[0].strip() for line in content if not line.startswith('//') and line is not '']
        self.source_code: list = content
        self.current_command: int = 0

    def _command(self):
        return self.source_code[self.current_command]

    def has_more_commands(self):
        if self.current_command < len(self.source_code):
            return True
        return False

    def advance(self):
        if self.has_more_commands():
            self.current_command += 1

    def command_type(self):
        if self._command().startswith('@'):
            return 'A_COMMAND'
        if self._command().startswith('('):
            return 'L_COMMAND'
        return 'C_COMMAND'

    def symbol(self):
        command = self._command()
        if command.startswith('@'):
            return command.split('@')[1]
        return command[command.find('(') + 1: command.find(')')]

    def dest(self):
        command = self._command()
        if command.find('=') is -1:
            return ''
        return command[0:command.find('=')]

    def comp(self):
        command = self._command()
        if command.find('=') is -1 and command.find(';') is -1:
            return command
        if command.find('=') is -1 and command.find(';') is not -1:
            return command[:command.find(';')]
        if command.find('=') is not -1 and command.find(';') is -1:
            return command[command.find('=') + 1:]
        return command[command.find('=') + 1:command.find(';')]

    def jump(self):
        command = self._command()
        if command.find(';') is -1:
            return ''
        return command[command.find(';') + 1:]
