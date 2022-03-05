#!/usr/bin/python3

import cmd, sys, os
import json
import shlex
# import models
from models.base_model import BaseModel
# from models.user import User
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review
from models import storage

dict_class = {"BaseModel": BaseModel()}

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "



    def emptyline(self):
        """Method for avoid errors on empty line"""
        pass
    def do_quit(self, arg):
        """Quit command to exit the program"""
        quit()
    def do_EOF(self, arg):
        """EOF Method"""
        return True
    def do_create(self, arg):
        """Under Development"""
        if arg in dict_class:
            print("hola si estoy")
            new_var = "{}()".format(arg)
            new_item= eval(new_var)
            new_item.save()
            print(new_item.id)
        elif len(arg) == 0:
            print("No existo")
        else:
            print("No toy")
    def do_show(self, arg):
        """Under Development"""
        if len(arg) == 0:
            print("no existo")
            return
        splitted_arg = arg.split()
        if splitted_arg[0] not in dict_class:
            print("no toy")
            return
        new_str = "{}.{}".format(splitted_arg[0], splitted_arg[1])
        recuento = storage.all()
        if new_str in recuento.keys():
            print(recuento[new_str])
        else:
            print("No toy")
        
    def do_destroy(self, arg):
        """Under Development"""
        print("Under developoment")
    def do_all(self, arg):
        """Under Development"""
        print("Under developoment")
    def do_update(self, arg):
        """Under Development"""
        print("Under developoment")
    def do_clear(self, arg):
        """Clear command"""
        os.system('clear')      

if __name__ == '__main__':
    HBNBCommand().cmdloop()