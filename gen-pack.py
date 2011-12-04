#!/usr/bin/python

import sys

from jinja2 import Environment, PackageLoader
from jinja2 import Template

def run(num_of_servers):
	env = Environment(loader=PackageLoader('gen-pack', ''))
	template = env.get_template('membase_template')
	print template.render(num_of_servers=num_of_servers)

def help():
	print "Usage:"
	print "gen-pack.py number_of_servers\n"
	print "i.e.: gen-pack.py 3\n"

def main():
	if len(sys.argv) < 2:
		help()
	else:
		run(int(sys.argv[1]))
	
if __name__ == "__main__":
	main()