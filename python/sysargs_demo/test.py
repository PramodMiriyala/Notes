"""__summay__"""
import sys
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("enter 3 arguments, this programme expects 3 args")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("please enter only 3 arguments, this programme only supports 3 args")
        sys.exit(1)
    else:
        print(f"{int(sys.argv[1])} + {int(sys.argv[2])} = {int(sys.argv[1]) + int(sys.argv[2])}")
