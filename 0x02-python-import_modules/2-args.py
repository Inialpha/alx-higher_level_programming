#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argv = sys.argv[1:]
    len = len(argv)
    if len == 0:
        print("{}".format("0 arguments."))
    else:
        print("{} {}".format(len, "arguments:" if len > 1 else "argument."))
        for i in range(len):
            pos = i + 1
            print("{}: {}".format(pos, argv[i]))
