#!/usr/bin/python3
""" This Module defines the console, which contains the
    entry point of the a command line interpreter.

    ===========
    class
    ===========

    HNBNCommand

    ===========
    Methods
    ===========

    do_quit()
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """the command interpeter class """
    
    prompt = "(hbnd) "

    def do_quit(self):
        """ ... """
        return True

    do_EOF = do_quit
    
HBNBCommand().cmdloop()
