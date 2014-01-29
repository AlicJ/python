#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Alic Jiang
#
# Created:     17/01/2014
# Copyright:   (c) Alic Jiang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import mymodule1
import mymodule2

print( (mymodule2.myage - mymodule1.myage) ==
       (mymodule2.year - mymodule1.year)  )

print("My name is", __name__)


