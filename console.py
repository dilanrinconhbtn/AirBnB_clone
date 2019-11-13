#!/usr/bin/python3
"""
Console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""

    prompt = '(hbnb)'

    def do_EOF(self, line):
        """exit"""
        return True

    def do_quit(self, line):
        """exit"""
        return True

    def emptyline(self):
        '''Empty'''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
