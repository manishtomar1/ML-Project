
import csv
import numpy as np
from sklearn import preprocessing
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt
#from sklearn.preprocessing import OneHotEncoder
#from sklearn.feature_selection import VarianceThreshold


if __name__ == "__main__":
    csv_path = "F:/mtech 1st sem/ml/ctr prediction/dstrain.csv"
    with open(csv_path, "rb") as f_obj:
        datax=[]
        datay=[]
        reader = csv.reader(f_obj)
        zz=1
        for row in reader: 
            if zz==1:
                zz+=1
                continue
            r=" ".join(row)
            b=[]
            b=r.split(' ')
            a=[]
            for i in range(0,len(b)-1):
                if i!=1:
                    a.append(b[i])
                if i==1:
                    k=b[i]
            datax.append(a)
            datay.append(k)
#    print datax
    print len(datax),len(datay),len(datax[0])

    le = preprocessing.LabelEncoder()
    c_datax=[]
    datax=np.asarray(datax)
    for i in range(0,len(datax[0])):
        le.fit(datax[:,i])
        c_datax.append(le.transform(datax[:,i]))
    
    c_datax=np.asarray(c_datax)
    c_datax=c_datax.T
    print len(c_datax),len(c_datax[0])

    colors=['red','blue']
    x=TSNE(n_components=2).fit_transform(c_datax)
#    x=[[1,1],[2,2]]
    for i in range(0,len(x)):
        print x[i][0],x[i][1],datay[i]
        if datay[i]=='0':
            plt.scatter(x[i][0],x[i][1],color=colors[0])
        else:
            plt.scatter(x[i][0],x[i][1],color=colors[1])
    plt.show()
#    plt.savefig("F:/mtech 1st sem/ml/ctr prediction/plotC")
    
#    enc = OneHotEncoder()
#    enc.fit(c_datax)
#    print enc.n_values_
#    print enc.transform(c_datax).shape
    
#    var_features=np.var(c_datax,axis=0)
#    for i in range(len(var_features)):
#        print (i+1),var_features[i]
#
#
#    sel = VarianceThreshold(threshold=7)
#    print sel.fit_transform(c_datax).shape
    
    
    