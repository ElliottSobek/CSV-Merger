import os
import sys
import csv

from os.path import basename


def main(argc=len(sys.argv), argv=sys.argv):
    if argc < 2:
        print("Usage: python3 " + basename(argv[0]) + " <filename.csv ...> <outfile>")
        return

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
