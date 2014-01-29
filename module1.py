#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Alic Jiang
#
# Created:     17/01/2014
# Copyright:   (c) Alic Jiang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import Test

def myreplace(old, new, s):
    return new.join(s.split(old))



Test.main(myreplace(",", ";", "this, that, and some other thing") == "this; that; and some other thing")
Test.main(myreplace(" ", "**", "Words will now be separated by stars.") == "Words**will**now**be**separated**by**stars.")