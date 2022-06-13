"""
Provide an interface for creating boilerplate code for scripts that will take command line arguments.

- Prompt the user for the name of their script.
- Description for the script.
- Add an argument
    - Is this argument positional or optional?
    - Give the argument a long name and a short name (if optional)
    - Is this argument required?
    - Type: int, float, string, flag
    - Number of args? (N, ?, *, +, default)
    - Default value?
    - Choices?
    - Write a help message for that argument
    - Belongs to mutually exclusive group (y/n).
    - Name of group (for mutually exclusive group only)
"""

import sys
from argunaut.Argument import Argument
from argunaut.ScriptWriter import ScriptWriter

def isYes(inputStr: str, default_if_empty: bool) -> bool:
    if inputStr.lower == 'yes' or inputStr.lower == 'y':
        isYes = True
    elif len(inputStr) == 0:
        isYes = default_if_empty
    else:
        isYes = False

    return isYes


def getShortName():
    short_name = input('Short name for argument (single letter) [None]:\n')

    # TODO: Prompt the user that they didn't provide a valid short name.
    if len(short_name) != 1:
        short_name = None
    
    return short_name


def getArgType():
    allowed_types = ['string', 'int', 'float', 'flag']
    arg_type = input('Argument type (string, float, int, flag): [string]:\n')

    # TODO: Prompt the user that they didn't specifiy a valid type.
    if arg_type not in allowed_types:
        arg_type = 'string'

    return arg_type


def getDefaultVal():
    default_val = input('Default value: [None]:\n')

    if (len(default_val) == 0):
        return None
    
    return default_val


def getNargs():
    allowed_nargs = ['?', '*', '+']
    nargs = input('Number for items allowed for this argument (N, ?, *, +) [single item]:\n')

    if type(nargs) != int and nargs not in allowed_nargs:
        nargs = None

    return nargs


def getChoices():
    choices = input('Limit to specific choices (separate options by commas) [Any]:\n')
    if len(choices) > 0:
        choices = [choice.strip() for choice in choices.split(',')]
    else:
        choices = None

    return choices

def getGroupName():
    group_name = input('If this option belongs to a mutually exclusive group, what is the group name? [None]:\n')
    if len(group_name) == 0:
        group_name = None
    
    return group_name


def getHelpMsg():
    help_msg = input('Provide a brief help message about this argument:\n')

    help_msg_complete = False
    while not help_msg_complete:
        if len(help_msg) > 0:
            help_msg_complete = True
        else:
            print('\nYou must provide a help message.')
            help_msg = input('Provide a brief help message about this argument:\n')

    return help_msg


def getScriptDescription():
    description = input('Provide a brief description of this script:\n')

    description_complete = False
    while not description_complete:
        if len(description) > 0:
            description_complete = True
        else:
            print('\nYou must provide a description.')
            description = input('Provide a brief description of this script:\n')

    return description

        
def addArgument(arg_name: str) -> Argument:
    arg = Argument(arg_name)
    positional = isYes(input('Is this a positional argument (y/n)? [yes]:\n'), True)

    if not positional:
        arg.long_name = '--' + arg.long_name
        arg.required = isYes(input('Is this argument required (y/n)? [no]:\n'), False)
        arg.short_name = None
    else:
        arg.required = True

    arg.help_msg = getHelpMsg()
    arg.arg_type = getArgType()
    arg.default_val = getDefaultVal()
    arg.nargs = getNargs()
    arg.choices = getChoices()
    arg.group_name = getGroupName()

    print(arg)

def main():
    script_name = input('Script name:\n')
    script_description = getScriptDescription()

    add_arg = True
    args: list[Argument] = []
    while add_arg:
        arg_name = input('New argument name (press <return> to stop adding arguments):\n')

        if (len(arg_name) == 0):
            add_arg = False
        else:
            args.append(addArgument(arg_name))

    if len(args) == 0:
        sys.exit('No arguments were provided. Aborting.')

    writer = ScriptWriter(script_name, script_description, args)
    writer.writeScript()


if __name__ == '__main__':
    main()
