#import sys

print(sys.argv[0])


try:
    value = int(sys.argv[1])
except ValueError:
    print('Not Integer')
