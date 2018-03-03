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
import csv

from os.path import basename


def main(argc=len(sys.argv), argv=sys.argv):
    if argc < 2:
        print("Usage: python3 " + basename(argv[0]) + " <filename.csv ...> <outfile>")
        return

    print("Merge CSV Copyright (C) 2018  Elliott Sobek\n"
          "This program comes with ABSOLUTELY NO WARRANTY.\n"
          "This is free software, and you are welcome to redistribute it under certain conditions.\n")

    for i in range(1, argc - 1):
        if not argv[i].endswith('.csv'):
            print("Error: Passed in file(s) must be comma separated value (csv) format")
            return

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
