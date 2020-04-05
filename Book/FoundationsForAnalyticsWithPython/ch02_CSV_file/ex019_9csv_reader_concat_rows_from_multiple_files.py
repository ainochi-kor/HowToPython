#!/usr/bin/env python3
#여러 파일의 데이터 합치기

import csv
import glob
import os
import sys

input_path = "C:/Users/AINOCHI/Desktop/Project/HowToPython/Book/FoundationsForAnalyticsWithPython/ch02_CSV_file/csv/"
output_file = "csv/ex019_9output.csv"

first_file = True
for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    print(os.path.basename(input_file))
    with open(input_file, 'r', newline='') as csv_in_file:
        with open(output_file, 'a', newline='') as csv_out_file:
            filereader = csv.reader(csv_in_file)
            filewriter = csv.writer(csv_out_file)
            if first_file:
                for row in filereader:
                    filewriter.writerow(row)
                first_file = False
            else:
                 header = next(filereader)
                 for row in filereader:
                     filewriter.writerow(row)