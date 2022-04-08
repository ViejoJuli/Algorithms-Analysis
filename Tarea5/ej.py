#!/usr/bin/env python3 
from collections import Counter
import sys

with open (sys.argv[1]) as f:
    lines=f.readlines()
string=''.join([str(item) for item in lines])
chars=list(Counter(string).keys())
freq=list(Counter(string).values())



# chars=list(Counter(sys.argv[1]).keys())
# freq=list(Counter(sys.argv[1]).values())
