#!/usr/bin/python3

import cmd, sys

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        quit()
    def do_EOF(self, arg):
        quit()
    def do_create(self, arg):
        print("Under developoment")
    def do_show(self, arg):
        print("Under developoment")
    def do_destroy(self, arg):
        print("Under developoment")
    def do_all(self, arg):
        print("Under developoment")
    def do_update(self, arg):
        print("Under developoment")

if __name__ == '__main__':
    HBNBCommand().cmdloop()