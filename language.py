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

def calculate4gramProb(context, symbol, fourgramData, trigramData):
    word = context + symbol
    fourCount = fourgramData.get(word)
    thirdCount = trigramData.get(context)
    prob = fourCount / thirdCount
    print(f"P({symbol}|{context}) = {prob}")   
    
def calculateLI(context, fourgramData, trigramData, bigramData, unigramData):
    ramuda1 = 0.1
    ramuda2 = 0.1
    ramuda3 = 0.2
    ramuda4 = 0.5
    Sum = unigramData.get("G") + unigramData.get("C") + unigramData.get("P")
    
    print(unigramData.get(context[3]) / Sum)
    print(bigramData.get(context[2:4]) / unigramData.get(context[2]))
    print(trigramData.get(context[1:4]) / bigramData.get(context[1:3]))
    prob1 = ramuda1 * (unigramData.get(context[3]) / Sum)
    prob2 = ramuda2 * (bigramData.get(context[2:4]) / unigramData.get(context[2]))
    prob3 = ramuda3 * (trigramData.get(context[1:4]) / bigramData.get(context[1:3]))
    prob4 = ramuda4 * (fourgramData.get(context) / trigramData.get(context[0:3]))
    
    prob =  prob1 + prob2 + prob3 + prob4
    print(f"{context}:{prob}")
    
if __name__ == "__main__":

    # CSVを読み込む
    unigramData = getData("1.csv")
    bigramData = getData("2.csv")
    trigramData = getData("3.csv")
    fourgramData = getData("4.csv")
    
# =============================================================================
# kadai(1)
# =============================================================================
    print("最尤推定")
    calculate4gramProb("PCC", "G", fourgramData, trigramData)
    calculate4gramProb("PCC", "C", fourgramData, trigramData)
    calculate4gramProb("PCC", "P", fourgramData, trigramData)

# =============================================================================
# kadai(2)
# =============================================================================
    print("線形補間法")
    calculateLI("PCCG", fourgramData, trigramData, bigramData, unigramData)
    calculateLI("PCCC", fourgramData, trigramData, bigramData, unigramData)
    calculateLI("PCCP", fourgramData, trigramData, bigramData, unigramData)



