#!/usr/bin/env python

def FuncOut(a,b):
    print "Hi! My name is %s and my age is %d" % (a,b)
    print "Hi! My name is {} an my age is {}".format(a,b)
    print "Hi! My name is", a + " and my age is", b
FuncOut('Mary',19)
