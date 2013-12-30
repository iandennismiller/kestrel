# Ian Dennis Miller

import sys, os, platform, glob

# find all the conf files in the given directory
base_path = sys.argv[1]
files = glob.glob(os.path.join(base_path, "*.conf"))

getmail_cmd = "/usr/bin/getmail --quiet --rcfile %s" % " --rcfile ".join(files)
os.system(getmail_cmd)
