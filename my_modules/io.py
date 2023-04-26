# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 15:37:35 2023

@author: User
"""
# Import CSV file
import csv

# Read input data
import csv
import pandas as pd

url = 'https://raw.githubusercontent.com/DanielINCE/ABM5/main/in.txt'
df = pd.read_csv(url,index_col=0)
#df = pd.read_csv(url)

print(df.head(5))


# Import IO
import io 
environment = io.read_data()



