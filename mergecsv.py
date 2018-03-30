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

from os import name, access, R_OK
from os.path import basename, getsize, exists, dirname, splitext
from sys import exit, argv
from optparse import OptionParser
from csv import writer


def gen_outfile(filepath, extension):
    out_dir = dirname(filepath)
    out_base = basename(filepath)
    base_outfile = splitext(out_base)[0]

    if out_dir:
        if name == "nt":
            return out_dir + '\\' + base_outfile + extension
        return out_dir + '/' + base_outfile + extension
    return out_dir + base_outfile + extension


def main():
    parser = OptionParser(usage="Usage: python3 %prog [options] <filename.csv ...> <outfile>", version="%prog 0.1")

    parser.add_option("-v", action="store_true", dest="vertical_flag", help="Merge files vertically")
    parser.add_option("-d", action="store_true", dest="diagonal_flag", help="Merge files diagonally")
    parser.add_option("-f", action="store_true", dest="force_flag", help="Force merge if an input file is empty")

    options, args = parser.parse_args()

    if len(args) is not 3:
        print("Usage: python3 " + basename(argv[0]) + " [-hvdf] <filename.csv ...> <outfile>")
        exit(1)

    in_files = args[:-1]
    out_file_name = args[-1]

    if options.vertical_flag and options.diagonal_flag:
        print("Error: more than one merge axis flags set")
        exit(1)

    extension = ".csv"

    for file in in_files:
        if not exists(file):
            print("Error: " + file + " does not exist")
            exit(1)
        if not file.endswith(extension):
            print("Error: " + file + " must be comma separated value (csv) format")
            exit(1)
        if not options.force_flag and not getsize(file):
            print("Error: " + file + " is empty")
            exit(1)

    if not out_file_name.endswith(extension):
        out_file_name = gen_outfile(out_file_name, extension)
    if access(out_file_name, R_OK):
        print("Error: " + out_file_name + " is readonly")
        exit(1)

    print("Merge CSV Copyright (C) 2018  Elliott Sobek\n"
          "This program comes with ABSOLUTELY NO WARRANTY.\n"
          "This is free software, and you are welcome to redistribute it under certain conditions.")

    outfile = open(out_file_name, 'w', encoding="utf-8", newline='')
    out_writer = writer(outfile)

    for in_filename in in_files:
        in_file = open(in_filename, 'r', encoding="utf-8", newline='')

        in_file.close()
    outfile.close()

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
