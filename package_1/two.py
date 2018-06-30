#import one
#from one import m1
from one import *

import sys
def m2():
    print("System path....",sys.path)
    print("Inside m2 of module two.py")
    m1()
    m1_2()
	
