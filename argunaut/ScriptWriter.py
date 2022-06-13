"""
Helper class for writing boilerplate code. Takes in a collection of Arguments and
outputs a script that parses them.
"""
from functools import reduce
from argunaut.Argument import Argument

class ScriptWriter:
    def __init__(self, name: str, desc: str, args: list) -> None:
        self.MAX_LINE_CHARS = 80

        self.name = name
        self.desc = desc
        self.args = args
        self.script = ''
    
    def writeScript(self):
        self.script += self.makeHeader()
        self.script += self.makeGetArgsFunc()
        self.script += self.makeMainFunc()

        with open(f'{self.name}.py', 'w') as f:
            f.write(self.script)

    # Break string at word boundry if it exceeds 80 characters
    def formatLongString(self, long_str: str, indent_lvl: int) -> str:
        if len(long_str) < 80:
            return long_str + '\n'

        words = long_str.split()
        formatted_str = ''
        line_words = []
        for word in words:
            if (reduce(lambda x, y: x + len(y), line_words, 0) + len(word)) < self.MAX_LINE_CHARS:
                line_words.append(word)
            else:
                formatted_str += self.indent(indent_lvl) + ' '.join(line_words) + '\n'
                line_words = [word]

        formatted_str += self.indent(indent_lvl) + ' '.join(line_words) + '\n'

        return formatted_str

    def indent(self, indent_lvl) -> str:
        return ' ' * 4 * indent_lvl

    def makeHeader(self) -> str:
        header = "import argparse\n\n"
        return header

    def makeGetArgsFunc(self) -> str:
        getArgs = "def getCommandLineArgs():\n"
        getArgs += self.indent(1) + "parser = argparse.ArgumentParser(description=\"\"\"\n"

        formatted_desc = self.formatLongString(self.desc, 2)
        getArgs += formatted_desc
        getArgs += self.indent(1) + "\"\"\")\n\n"

        # TODO: Add args
        getArgs += self.indent(1) + "return parser.parse_args()\n\n"

        return getArgs
        
    def addArg(self, arg) -> str:
        return ''

    def makeMainFunc(self) -> str:
        return ''
