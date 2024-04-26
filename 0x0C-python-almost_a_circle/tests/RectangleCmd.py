#!/urs/bin/python3

import cmd
from models.rectangle import Rectangle

class RectangleCmd(cmd.Cmd):
    prompt = 'Rectangle > '
    intro = 'Welcome to The Rectangle CLI. Type help or ? to list commands. '

    def do_create(self, arg):
        """create a new rectangle. Usage: create <width> <height> [<x> <y>]"""
        arts = arg.split()
        if len(args) < 2 or len(args) > 4:
            print("Invalid number of arguments. Usage: Create <width> <height> [<x> <y>]")
            return
        width = int(args[0])
        height = int(args[1])
        x = int(args[2]) if len(args) > 2 else 0
        y = int(args[3]) if len(args) > 3 else 0
        rectangle = Rectangle(width, heigh, x, y)
        print("Rectangle Created with ID:", rectangle.id)
    def do_exit(self, arg):
        """Exit the CLI"""
        print("Exiting...")
        return(True)
if __name__ == '__main__':
    RectangleCmd().cmdloop()
