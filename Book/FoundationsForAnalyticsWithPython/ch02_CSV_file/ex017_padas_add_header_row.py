#!/usr/bin/env python3
import pandas as pd
import sys

input_file = 'csv/supplier_data_no_header_row.csv'
output_file = 'csv/ex017_pandas_output.csv'

header_list = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
data_frame = pd.read_csv(input_file, header=None, names=header_list)

data_frame.to_csv(output_file,index=False)