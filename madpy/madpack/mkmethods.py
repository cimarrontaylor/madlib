#!/usr/bin/python
#
# Script/module to call 'make install' for each MADlib method port
# in the MADlib Config.yml file.

import yaml
import os
import subprocess
import madpy
import madpy.madpack.configyml
    
def install_methods(mkarg, conf):
    for m in conf['methods']:
        mdir = madpy.__path__[0]+'/../madlib/' + m['name'] + '/src/' + m['port'] + '/'
        # print "changing directory to " + mdir
        curdir = os.getcwd()
        try:
            os.chdir(mdir)
        except OSError:
            print "directory " + mdir + " does not exist"
            exit(2)            
        try:
            install = yaml.load(open('Install.yml'))
        except:
            print "method " + m['name'] + " misconfigured: missing Install.yml file"
            sys.exit(2)
        try:
            install['module']
        except:
            print "method " + m['name'] + " misconfigured: Install.yml missing module"
            sys.exit(2)
        if install['module'] != None:
            subprocess.call(['make', mkarg], stderr = subprocess.PIPE)
        os.chdir(curdir)
            
if __name__ == "__main__":
    install_methods()