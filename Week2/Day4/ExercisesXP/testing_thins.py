import os
import sys

print(sys.argv[0])
print(os.path.abspath(sys.argv[0]))
print(os.path.dirname(os.path.abspath(sys.argv[0])))