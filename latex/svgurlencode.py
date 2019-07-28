from urllib.parse import quote
import sys

with open(sys.argv[1]) as fin:
  lines = fin.readlines()

s = quote("".join(lines))
print(f"![image](data:image/svg+xml,{s})")
