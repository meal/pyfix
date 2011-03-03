#!/usr/bin/env python
import sys, os, io
import MySQLdb
import settings

def import_module(name, package=None):
    if name.startswith('.'):
        if not package:
            raise TypeError("relative imports require the 'package' argument")
        level = 0
        for character in name:
            if character != '.':
                break
            level += 1
        name = _resolve_name(name[level:], package, level)
    __import__(name)
    return sys.modules[name]

def main():
	print "pyfix "+settings.VERSION+" - tools to manage postfix users in mysql database\n"
	
	if 1 == len(sys.argv):
		print "Available commands:"
		path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'commands'))
		for f in os.listdir(path):
			if not f.startswith('_') and f.endswith('.py'):
				print f.replace('.py', '')
		print "Type help <command> for help on a specific command."
	else:
		try:
			if (3 == len(sys.argv)) and ('help' == sys.argv[1]):
				command = sys.argv[2]
				help = True
			else:
				command = sys.argv[1]
				help = False
				
			module = import_module("commands."+command)
			
			if help:
				print "Help for "+command+":"
				module.help()
			else:
				module.execute()
		except ImportError:
			print "Unknown command "+command
if __name__ == "__main__":
    main()
