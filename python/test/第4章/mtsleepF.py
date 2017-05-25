#!/bin/bash/env python

from atexit import register
from random import randrange
from threading import Thread, currentThread
from time import sleem, ctime

class CleanOutputSet(set):
    def __str__(self):
        return ','.join(x for x in self)

loops = (randrange(2,5) for in xrange(randrange(3,7)))
