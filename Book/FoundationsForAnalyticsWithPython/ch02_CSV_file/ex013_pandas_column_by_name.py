#!/usr/bin/env python3
import pandas as pd
import sys

input_file = 'csv/supplier_data.csv'
output_file = 'csv/ex013_pandas_output.csv'

data_frame = pd.read_csv(input_file)
data_frame_columns_by_name = data_frame.loc[:, ['Invoice Number', 'Purchase Date']]

data_frame_columns_by_name.to_csv(output_file,index=False)