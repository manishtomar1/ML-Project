# -*- coding: utf-8 -*-
"""
Created on Wed Oct 04 02:30:24 2017

@author: Dell1
"""

import csv
if __name__ == "__main__":
    csv_path = "F:/mtech 1st sem/ml/ctr prediction/train.csv"
    with open(csv_path, "rb") as f_obj:
        data=[]
        reader = csv.reader(f_obj)
        i=1
        for row in reader:
            data.append(" ".join(row))
#            print " ".join(row)
            if(i>2000000):
                break
            i+=1
    with open('F:/mtech 1st sem/ml/ctr prediction/dstrain.csv','wb') as file:
        w=csv.writer(file)
        for j in range(len(data)):
            w.writerow(data[j])
    

    