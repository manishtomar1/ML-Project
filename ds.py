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
            data.append(row)
#            print " ".join(row)
            if(i>200000):
                break
            i+=1
    print data
    with open('F:/mtech 1st sem/ml/ctr prediction/dstrain.csv','wb') as file:
        w=csv.writer(file)
        for j in range(len(data)):
            a=str(data[j])
            b=""
            for k in range(len(data[j])):
                b=b+str(data[j][k])+" "
            b=b.split(' ')
            w.writerow(b)
    

    