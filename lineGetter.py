import sys

#########################################
# This program outputs the lines that
# have have exactly sys.argv[1] columns.
#########################################

for arg in sys.argv[2:]:
    with open(arg) as fin:
        for line in fin:
            sections = line.split(',')
            if not (sections[2] == ''):
                sys.stdout.write(line)