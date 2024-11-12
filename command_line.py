import sys

import convert

sum = 0
for idk in range(1, len(sys.argv)):
    num = convert.str_to_float(sys.argv[idk])
    if num != None:
        sum += num

if __name__ == '__main__':
    print(sum)