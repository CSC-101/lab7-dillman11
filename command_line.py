import sys

import convert

sum = 0
for idk in range(1, len(sys.argv)):
    float_num = convert.str_to_float(sys.argv[idk])
    if float_num != None:
        sum += float_num
print(sum)

if __name__ == '__main__':
    print(sys.argv)