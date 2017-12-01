import sys

#########################################
# This program outputs the lines that
# have have exactly sys.argv[1] columns.
#########################################

for arg in sys.argv[1:]:
    with open(arg) as fin:
        for line in fin:
            sections = line.split(',')
            if sections[2] == '' or sections[4] == '':
                sys.stdout.write(line)