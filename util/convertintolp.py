#!/usr/bin/python3

# Written by Tobias Achterberg (2019-01-30)

import sys

for fname in sys.argv[1:]:
    print("Input file:", fname)

    with open(fname) as f:
        # number of variables
        line = f.readline()
        nvars = int(line)
        print("   nvars:", nvars)

        # linear objective c
        line = f.readline()
        c = [float(v) for v in line.split()]
        if len(c) != nvars:
            print("   error: invalid number of entries in c vector")
            sys.exit(1)

        # quadratic objective Q
        Q = []
        for line in f:
            Q.append([float(v) for v in line.split()])
            if len(Q[-1]) != nvars:
                print("   error: invalid number of entries in Q vector row", len(Q))
                sys.exit(1)
        if len(Q) != nvars:
            print("   error: invalid number of rows in Q vector")
            sys.exit(1)

    # write LP file
    oname = fname+".lp"
    with open(oname, 'w') as of:
        of.write("Minimize\n")
        for j, v in enumerate(c):
            of.write(f' {v:+g} x{j:d}')
            if (j+1) % 8 == 0:
                of.write("\n")
        if nvars % 8 != 0:
            of.write("\n")
            
        of.write(" + [")
        for i, q in enumerate(Q):
            for j, v in enumerate(q):
                of.write(f' {v:+g} x{i:d} * x{j:d}')
                if (nvars*i + j+1) % 8 == 0:
                    of.write("\n")
        of.write(" ] / 2\n")

        of.write("Subject To\n")
        of.write("Bounds\n")
        for j in range(nvars):
            of.write(f' 0 <= x{j:d} <= 1\n')
        of.write("End\n")

