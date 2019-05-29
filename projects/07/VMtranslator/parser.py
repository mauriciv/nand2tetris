class Parser():

    arithmetic_commands = ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']

    def __init__(self, file):
        content = [line.strip() for line in file.readlines()]
        content = [line.split('//')[0].strip() for line in content if not line.startswith('//') and line is not '']
        self.source_code: list = content
        self.current_command: int = 0
    
    def _command(self):
        return self.source_code[self.current_command]

    def has_more_commands(self):
        return self.current_command < len(self.source_code)

    def advance(self):
        if self.has_more_commands():
            self.current_command += 1

    def command_type(self):
        if self._command() in self.arithmetic_commands:
            return 'C_ARITHMETIC'
        if self._command().startswith('push'):
            return 'C_PUSH'
        if self._command().startswith('pop'):
            return 'C_POP'
        if self._command().startswith('label'):
            return 'C_LABEL'
        if self._command().startswith('goto'):
            return 'C_GOTO'
        if self._command().startswith('if-goto'):
            return 'C_IF'
        if self._command().startswith('function'):
            return 'C_FUNCTION'
        if self._command().startswith('return'):
            return 'C_RETURN'
        if self._command().startswith('call'):
            return 'C_CALL'
        raise ValueError('Unrecognized vm command.')

    def arg1(self):
        if self.command_type() is 'C_RETURN':
            return ''
        if self.command_type() is 'C_ARITHMETIC':
            return self._command()
        return self._command().split(' ')[1]

    def arg2(self):
        if self.command_type() is not 'C_PUSH'\
        and self.command_type() is not 'C_POP'\
        and self.command_type() is not 'C_FUNCTION'\
        and self.command_type() is not 'C_CALL':
            return ''
        return self._command().split(' ')[2]