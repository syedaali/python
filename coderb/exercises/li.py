for i in xrange(1,101):
    if (i % 4 == 0 ) and (i % 6 == 0):
        print "LinkedIn"
        continue
    if i % 4 == 0:
        print "Linked"
        continue
    if i % 6 == 0:
        print "In"
        continue
    print i


