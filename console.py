#!/usr/bin/python3
"""file contains code for console program"""


import re
import ast
import models
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.review import Review
from datetime import datetime


classes = ["BaseModel", "User", "Place", "City", "State", "Amenity", "Review"]


class HBNBCommand(cmd.Cmd):
    '''contains the entry point of the command interpreter'''
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """Command to also exit the program\n"""
        return True

    def emptyline(self):
        """does nothing when no command is given\n"""
        return False

    def do_create(self, arg):
        """creates a new instance of BaseModel, saves it to the JSON file
        and prints the id"""
        args = arg.split()  # splits the argument using whitespace
        if len(args) < 1:
            print("** class name missing **")
            return False
        if args[0] not in classes:
            print("** class doesn't exist **")
            return False
        else:
            new_instance = eval(args[0] + "()")
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """prints the string representation of an instance based on
        the classname and id"""
        args = arg.split()  # splits the argument using whitespace
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) > 1:
            key = args[0] + "." + args[1]
            for obj in models.storage.all().keys():
                if obj == key:
                    print(models.storage.all()[key])

    def count(self, line):
        """
        This counts the instances of a certain class
        """
        cmd_list = split(line, ".")
        class_name = cmd_list[0]
        if class_name not in classes:
            raise NameError("** class doesn't exist **")
        else:
            counts = 0
            for key in models.storage.all():
                keyval = key.split(".")[0]
                if keyval == class_name:
                    counts += 1
            print(counts)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        if not arg:
            print("** class name missing **")
            return
        argv = arg.split()  # splits arguments using whitespace as seperator
        if argv[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(arg) < 2:
            print("** instance id missing **")
            return
        else:
            try:
                key = argv[0] + "." + argv[1]
                models.storage.all().pop(key)
                models.storage.save()
            except Exception:
                print("** no instance found **")
            finally:
                return

    def default(self, line):
        """
        This takes care of all self defined functions
        """
        inst_ids = re.search(r'\d[a-z0-9-]+', line)
        if inst_ids:
            inst_id = inst_ids.group(0)
        cmd_list = line.split(".")
        if len(cmd_list) == 2:
            class_name = cmd_list[0]
            if class_name in classes:
                if cmd_list[1] == "count()":
                    self.count(class_name)
                elif cmd_list[1] == "all()":
                    self.do_all(class_name)
                elif cmd_list[1][:4] == "show":
                    self.do_show("{} {}".format(class_name, inst_id))
                elif cmd_list[1][:7] == "destroy":
                    self.do_destroy("{} {}".format(class_name, inst_id))
                elif cmd_list[1][:6] == "update":
                    cmd_attrs = line.split(",")
                    if cmd_attrs[1][1] == "{":
                        dict_vals = ast.literal_eval(
                                re.search(r'({.+})', line).group(0))
                        for key, value in dict_vals.items():
                            self.do_update("{} {} {} {}".format(
                                class_name, inst_id, key, value))
                    else:
                        cmd_attr = cmd_attrs[1].strip()
                        cmd_attr1 = cmd_attrs[2].split(")")[0]
                        self.do_update("{} {} {} {}".format(
                            class_name, inst_id, cmd_attr, cmd_attr1))

    def do_all(self, arg):
        '''Prints all string representation of all instances based or
        not on the class name'''
        if not arg:
            list_inst = []
            for key, val in models.storage.all().items():
                list_int.append(str(val))
            if not list_inst:
                print("storage is empty!")
                return
            else:
                print(list_inst)
                return
        argv = arg.split()
        if argv[0] not in classes:
            print("** class doesn't exist **")
            return
        else:
            list_inst = []
            for key, val in models.storage.all().items():
                if str(key.split('.')[0]) == argv[0]:
                    list_inst.append(str(val))
            if not list_inst:
                return
            else:
                print(list_inst)
                return

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)"""
        if not arg:
            print("** class name missing **")
            return
        argv = shlex.split(arg)
        if argv[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(argv) == 1:
            print("** instance id missing **")
            return
        else:
            try:
                key = argv[0] + "." + argv[1]
                if key in models.storage.all():
                    models.storage.all()[key]
            except Exception:
                print("** no instance found **")
                return
        if len(argv) == 2:
            print("** attribute name missing **")
            return
        elif len(argv) == 3:
            print("** value missing **")
            return
        else:
            key = argv[0] + "." + argv[1]
            try:
                try:
                    value = int(argv[3])
                except ValueError:
                    value = float(argv[3])
            except ValueError:
                value = argv[3].strip(":\"'")
            attr = argv[2].strip(":\"'")
            setattr(models.storage.all()[key], attr, value)
            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
