import sys
import subprocess
import pkg_resources
import subprocess

required = {}
def checkRequire(required):
        
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed

    if missing:
        try:
            python = sys.executable
            subprocess.check_call(['pip', 'install', *missing])
        except subprocess.CalledProcessError as e:
            print(e)
