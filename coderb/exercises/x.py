mylist = []
with open (infile,'r') as fh:
    for each_line in fh:
        mylist.append = each_line.split("",2)
        mylist

        #
        (month, day, hh_mm_ss, other) = 'Jan 20 05:22:09 fakehost cs3[31163]:'.split(' ')[:4]
        hh_mm = ":".join(hh_mm_ss.split(':')[:2])  # 05:22

        x = month.join(day)



