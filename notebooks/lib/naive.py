import atexit
import numpy as np


# data storage
# one in-memory set

# while 1:
#  generate random permutation
#  check: in set?
#  add to set
def run(n, deck_size=52, verbose=False):
    ''' RUNTIME DATA '''
    i = 0
    collision = False
    visited = set()


    ''' EXIT SIGHANDLER '''
    def its_over():
        if collision:
            print "Ran %s steps" % i
            print "Found a collision!"
        elif verbose:
            print "Ran %s steps" % i
            print "Did not find a collision"


    ''' MAIN PROGRAM '''
    atexit.register(its_over)

    while i < n:
        perm = tuple(np.random.permutation(deck_size))
        if perm in visited:
            collision = True
            print "COLLISION FOUND!"
            print "After %s steps" % i
            print "%s" % str(perm)
        visited.add(perm)
        i += 1

    its_over()

