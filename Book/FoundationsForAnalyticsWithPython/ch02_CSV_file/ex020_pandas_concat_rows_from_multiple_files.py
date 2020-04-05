#!/usr/bin/env/ python3
import pandas as pd
import glob
import os
#import sys

input_path = "csv"
output_file = "csv/ex020_pandas_output.csv"

all_files = glob.glob(os.path.join(input_path, 'sales_*'))

all_data_frame = []
for file in all_files:
    data_frame = pd.read_csv(file, index_col=None)
    all_data_frame.append(data_frame) #all_data_frame에 data_frame에 든 csv 값을 append함.
data_frame_concat = pd.concat(all_data_frame, axis=0, ignore_index=True) #수직방향으로 data_frame 3개의 배열을 붙여버림.
data_frame_concat.to_csv(output_file, index = False)