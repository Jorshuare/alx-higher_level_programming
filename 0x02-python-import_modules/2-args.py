#!/usr/bin/python3
def print_arg(argv):
    n = len(argv) - 1
    if n == 0:
        print("{:d} arguments.".format(n))
    else:
        if n == 1:
            print("{:d} argument:".format(n))
            for j in range(1, n + 1):
                print("{:d}: {:s}".format(j, argv[j]))
        else:
            print("{:d} arguments:".format(n))
            i = 1
            while i <= n:
                print("{:d}: {:s}".format(i, argv[i]))
                i += 1


if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
