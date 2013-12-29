# Ian Dennis Miller

import sys, os, platform
from sievelib.parser import Parser
from sievelib.commands import ActionCommand, add_commands

# add the header-modifying command here

class SetflagCommand(ActionCommand):
    #is_extension = True
    args_definition = [
        {"name": "flag",
        "type": ["string"],
        "required": True}
    ]

add_commands(SetflagCommand)

p = Parser()
with(open("sieve/default.sieve")) as f:
    if p.parse(f.read()):
        print "parse OK"
    else:
        print "parser error"
        print p.error

# TODO: call with command line arguments
