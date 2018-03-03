#!/usr/bin/python3

#     Merge CSV; Merge multiple CSV files together
#     equivalent will be generated.
#     Copyright (C) 2018  Elliott Sobek
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

import os
import sys
import getopt
import csv

from os.path import basename


def main(argc=len(sys.argv), argv=sys.argv):
    base_name = basename(argv[0])

    if 4 < argc or 2 > argc:
        print("Usage: python3 " + base_name + " [-hvd] <filename.csv ...> <outfile>")
        sys.exit(1)

    try:
        opts, args = getopt.getopt(argv[1:], "hvd")
    except getopt.GetoptError as e:
        print(e.msg)
        sys.exit(1)

    vertical_flag = False
    diagonal_flag = False

    for opt, args in opts:
        if opt == "-h":
            print("Usage: python3 " + base_name + " [-hvd] <filename.csv ...> <outfile>\n\n"
                  "Default merge axis is horizontal (x axis)\n"
                  "\t-h\tHelp\n\n"
                  "\t-v\tMerge files vertically\n\n"
                  "\t-d\tMerge files diagonally\n\n")
            sys.exit()
        elif opt == "-v":
            vertical_flag = True
            print("WIP")
        elif opt == "-d":
            diagonal_flag = True
            print("WIP")

    if vertical_flag and diagonal_flag:
        print("Error: more than one merge axis flags set")
        sys.exit(1)

    print("Merge CSV Copyright (C) 2018  Elliott Sobek\n"
          "This program comes with ABSOLUTELY NO WARRANTY.\n"
          "This is free software, and you are welcome to redistribute it under certain conditions.\n")

    for i in range(1, argc - 1):
        if not argv[i].endswith('.csv'):
            print("Error: Passed in file(s) must be comma separated value (csv) format")
            return

    # if os.stat(argv[1]).st_size == 0 and os.stat(argv[2]).st_size == 0:
    #     output = open(argv[3], 'w', newline='')
    #     writer = csv.writer(output)
    #     writer.writerow(['Error: no data was provided'])
    #     output.close()
    #     return
    # elif os.stat(argv[1]).st_size == 0:
    #     copyfile(argv[2], argv[3])
    #     return
    # elif os.stat(argv[2]).st_size == 0:
    #     copyfile(argv[1], argv[3])
    #     return

    filename = sys.argv[-1]

    if not filename.endswith('.csv'):
        filename = filename.split(".")[0]
        filename += ".csv"

    outfile = open(filename, 'wb', newline='')
    writer = csv.writer(outfile)

    for i in range(1, argc - 1):
        if not os.stat(argv[i]).st_size:
            continue
    outfile.close()


main()
