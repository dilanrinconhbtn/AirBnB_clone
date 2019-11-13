#!/usr/bin/env python3
""" Console """

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
dic = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
       'State': State, 'City': City, 'Amenity': Amenity,
       'Review': Review}


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """exit"""
        return True

    def do_quit(self, line):
        """exit"""
        return True

    def emptyline(self):
        '''Empty'''
        pass

    def do_create(self, obj):
        """ Create a new object """
        if obj is None or len(obj) == 0:
            print("** class name missing **")
            return
        if obj in dic:
            new_obj = dic[obj]()
            new_obj.save()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, obj):
        """ Prints an object"""
        if obj is None or len(obj) == 0:
            print("** class name missing **")
            return
        l = obj.split()
        if len(l) < 2:
            print("""** instance id missing **""")
            return
        if l[0] not in dic:
            print("** class doesn't exist **")
            return
        a_o = models.storage.all()
        key = str(l[0]) + "." + str(l[1])
        if key in a_o:
            print(a_o[key])
        else:
            print("** no instance found **")

    def do_destroy(self, obj):
        """ Destroy an object """
        if obj is None or len(obj) == 0:
            print("** class name missing **")
            return
        l = obj.split()
        if len(l) < 2:
            print("""** instance id missing **""")
            return
        if l[0] not in dic:
            print("** class doesn't exist **")
            return
        a_o = models.storage.all()
        key = str(l[0]) + "." + str(l[1])
        if key in a_o:
            del(a_o[key])
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, obj):
        """ Prints all """
        if obj is None or len(obj) == 0:
            print("** class name missing **")
            return
        objs = obj.split()

        if objs[0] not in dic:
            print("** class doesn't exist **")
            return
        a_o = models.storage.all()
        l = []
        for key, val in a_o.items():
            ob_n = val.__class__.__name__
            if ob_n == objs[0]:
                l.append(str(val))
            print(l)
if __name__ == '__main__':
    HBNBCommand().cmdloop()
