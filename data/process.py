import pandas as pd
import csv
df = pd.read_csv('./dev.txt',sep = '\t',header=None,encoding='utf-8',names = ['car3','company','abstract','article'])
