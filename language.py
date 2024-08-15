# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 11:22:12 2024

@author: tack1
"""

import numpy as np
import csv

def getData(data_name):
    ngram_data = {}
    with open(data_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            ngram, count = row
            ngram_data[ngram] = int(count)
    return ngram_data

def caluculate4gramProb(context, symbol, fourgramData, trigramData):
    word = context + symbol
    fourCount = fourgramData.get(word)
    thirdCount = trigramData.get(context)
    prob = fourCount / thirdCount
    print(f"P({symbol}|{context}) = {prob}")    

if __name__ == "__main__":

    # CSVを読み込む
    data1 = getData("1.csv")
    data2 = getData("2.csv")
    data3 = getData("3.csv")
    data4 = getData("4.csv")

    # データ部を取得
    print(data1)
    print(data2)
    print(data3)
    print(data4)
    
# =============================================================================
#     kadai(1)
# =============================================================================
    caluculate4gramProb("PCC", "G", data4, data3)
    caluculate4gramProb("PCC", "C", data4, data3)
    caluculate4gramProb("PCC", "P", data4, data3)

