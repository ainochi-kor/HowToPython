#!/usr/bin/env python3
import pandas as pd
import sys

#input_file = sys.argv[1]
#output_file = sys.argv[2]
input_file = "csv/supplier_data.csv"
output_file = "csv/Week4_04.csv"

data_frame = pd.read_csv(input_file)
data_frame_value_matches_pattern = data_frame.ix[data_frame['Invoice Number']\
    .str.startswith("001-"), :]
data_frame_value_matches_pattern.to_csv(output_file,index=False)