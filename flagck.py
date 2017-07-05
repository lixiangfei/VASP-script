#!/bin/env python

import re

file_name = 'POSCAR'

with open(file_name) as input_file:
    content = input_file.readlines()

pattern = re.compile('\s+')
pre_flag = []
flag = []
print ""
print "Atom_id                      Content"
print "------------------------------------------"
for i in xrange(9, len(content)):
    temp = pattern.split(content[i].strip())
    length = len(temp)

    if length == 1:
        exit(0)

    if length != 6:
        print "-----------"
        print "%4d:    %s" % (i - 8, content[i].strip())
        print "-----------"
        continue

    if len(pre_flag) == 0:
        pre_flag = [temp[3], temp[4], temp[5]]
        flag = [temp[3], temp[4], temp[5]]
    else:
        flag = [temp[3], temp[4], temp[5]]

    if flag == pre_flag:
        continue
    else:
        pre_flag = flag
        print "%4d:    %s" % (i - 9, content[i - 1].strip())
        print "%4d:    %s" % (i - 8, content[i].strip())
        print "-----------"

print ""
