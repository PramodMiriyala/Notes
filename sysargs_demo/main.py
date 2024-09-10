#!/usr/bin/python3
import sys

if len(sys.argv) < 3:
    print("enter 3 arguments, this progrom expects 3 args")
    exit(1)
elif len(sys.argv) > 3:
    print("please enter only 3 arguments, this progrom only supports 3 args")
    exit(1)
else:
    print(f"{sys.argv[1]} {sys.argv[2]}")
