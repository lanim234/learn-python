import sys

print(sys.argv[0])

print(int(sys.argv[1]) + int(sys.argv[2]))

try:
    value = int(sys.argv[1])
except ValueError:
    print('Not Integer')
