#!/usr/bin/env python
#NOTE: to make executable, put in terminal:
# chmod +x joints_demo.py
# test the parser :)
from parser import Parser
parser = Parser("testem.bt")
print(len(parser.parseFile()))