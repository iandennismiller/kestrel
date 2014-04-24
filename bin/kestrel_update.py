# Ian Dennis Miller

import sys, os, platform, shutil
from distutils.dir_util import copy_tree
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

def copy_getmail(base_path):
    "copy all files from getmail/*.d into ~/.getmail"

    paths = [
        "0001.d",
        "0005.d",
        "0015.d",
        "0100.d",
        "0300.d",
        "0600.d",
        "2400.d",
        ]

    getmail_path = os.path.expanduser("~/.getmail")

    for path in paths:
        copy_tree(
            os.path.join(base_path, "getmail", path),
            os.path.join(getmail_path, path)
            )

def copy_sieve(base_path):
    sieve_path = os.path.expanduser("~/sieve/default.sieve")
    os.system("cat sieve/??-*.sieve > /tmp/default.sieve")

    p = Parser()
    with(open("/tmp/default.sieve")) as f:
        if p.parse(f.read()):
            print "parse OK"
            shutil.copy2("/tmp/default.sieve", sieve_path)
        else:
            print "parser error"
            print p.error

def main():
    # first, determine which directory we're operating on
    if len(sys.argv) == 1:
        base_path = os.getcwd()
    elif len(sys.argv) == 2:
        base_path = sys.argv[1]
    else:
        print "usage: kestrel_update.py [base_path]"
        sys.exit()

    # now copy all the files
    copy_getmail(base_path)
    copy_sieve(base_path)

main()
