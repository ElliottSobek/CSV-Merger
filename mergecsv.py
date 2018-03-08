#!/usr/bin/python3

#     Merge CSV; Merge multiple CSV files together
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

import sys
import csv

from os.path import basename, getsize, exists
from optparse import OptionParser


def main():
    parser = OptionParser(usage="Usage: python3 %prog [options] <filename.csv ...> <outfile>", version="%prog 0.1")
    parser.add_option("-v", action="store_true", dest="vertical_flag", help="Merge files vertically")
    parser.add_option("-d", action="store_true", dest="diagonal_flag", help="Merge files diagonally")
    parser.add_option("-f", action="store_true", dest="force_flag", help="Force merge if an input file is empty")

    options, args = parser.parse_args()

    if len(args) is not 3:
        print("Usage: python3 " + basename(sys.argv[0]) + " [-hvdf] <filename.csv ...> <outfile>")
        sys.exit(1)

    in_files = args[:-1]
    out_file = args[-1]

    if options.vertical_flag and options.diagonal_flag:
        print("Error: more than one merge axis flags set")
        sys.exit(1)

    for file in in_files:
        if not exists(file):
            print("Error: " + file + " does not exist")
            sys.exit(1)
        if not file.endswith('.csv'):
            print("Error: " + file + " must be comma separated value (csv) format")
            sys.exit(1)
        if not options.force_flag and not getsize(file):
            print("Error: " + file + " is empty")
            sys.exit(1)

    if not out_file.endswith('.csv'):
        print("Error: " + out_file + " must be comma separated value (csv) format")
        sys.exit(1)

    print("Merge CSV Copyright (C) 2018  Elliott Sobek\n"
          "This program comes with ABSOLUTELY NO WARRANTY.\n"
          "This is free software, and you are welcome to redistribute it under certain conditions.\n")

    # if getsize(argv[arg_index]) and getsize(argv[arg_index + 1]):
    #     output = open(argv[3], 'w', encoding='utf-8', newline='')
    #     writer = csv.writer(output)
    #     writer.writerow(['Error: no data was provided'])
    #     output.close()
    #     return
    # elif getsize(argv[arg_index]):
    #     # copyfile(argv[2], argv[3])
    #     return
    # elif getsize(argv[arg_index + 1]):
    #     # copyfile(argv[1], argv[3])
    #     return

    # outfile = open(filename, 'wb', newline='')
    # writer = csv.writer(outfile)
    # outfile.close()


main()
