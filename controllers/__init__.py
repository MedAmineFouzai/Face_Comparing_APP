'''
The controller initialization script
Imports all the files in the folder directly
To import modules, kindly include them in modules.py in the current folder
'''

from os.path import dirname,basename, isfile
import glob
modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and basename(f)!="__init__.py" and basename(f)!="modules.py"]

from . import *