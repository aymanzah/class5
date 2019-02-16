#!/usr/bin/env python

# 1.load a dataset from a file
# 2."organize that file so we can access columns *or* rows of it easily
# 3.compute some "summary statistics" about the dataset
# 4.print those summary statistics

# 1.load a dataset
# 1a. accept arbitrary filename as argument
# 1b. load the file

#import argparse
from argparse import ArgumentParser

parser = ArgumentParser(description='A CVS reader + stats maker')
parser.add_argument('csvfile', 
                    help='Path to the input csv file.')

parsed_args = parser.parse_args()
#print (parsed_args)
#print (parsed_args.csvfile)

my_csv_file = parsed_args.csvfile

import os

#if os.path.isfile(my_csv_file):
#    print('yay its real')
#else:
#    print ('give real file')

assert os.path.isfile(my_csv_file),"please give us a real file"
print('woot, the file exists')

# 1b. loadthe file
import pandas as pd

data= pd.read_csv(my_csv_file, sep='\s+|,', header = None)
print(data.head())

#for item in dir(data):
#    print(item)

print(data.shape)

#2 "organize that file so we can access columns *or* rows of it easily
#use of iloc: https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/

# 2A. ACCESS any row

print (data.iloc[3:5,:]) # inclusive the first value 3 but exclusive the last value 5

# 2b access any column

print (data.iloc[:3,-2:]) #-2 the last two

# 2c access any value

print(data.iloc[3,4])


# 4.print those summary statistics

import numpy as np

print (np.mean(data))
print (np.std(data))
