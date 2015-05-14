#coding=utf-8
__author__ = 'zhangchao'

from numpy import *


def loadDataSet(fileName,delim='t'):
    fr=open(fileName)
    stringArr=[line.strip().split(delim) for line in fr.readlines()]
    datArr=[map(float,line) for line in stringArr]
    return mat(datArr)

def pca(dataMat,topNfeat=9999999):
    meanVals=mean(dataMat,axis=0)
    meanRemoved=dataMat-meanVals
    covMat=cov(meanRemoved,rowvar=0)
    eigVals,eigVects=linalg.eig(mat(covMat))
    eigValInd=argsort(eigVals)
    eigValInd=eigValInd[:-(topNfeat+1):-1]
    redEigVects=eigVects[:,eigValInd]
    lowDDataMat=meanRemoved*redEigVects
    reconMat=(lowDDataMat*redEigVects.T)+meanVals
    return lowDDataMat,reconMat


def loaddata(file):
    t="F:/guangpu.txt"
    f = open(file)
    stringArr=[line.strip().split('\t') for line in f.readlines()]
    datArr=[map(float,line) for line in stringArr]
    data=mat(datArr)
    return data


def pca2(dataMat, topNfeat=5):
    meanVals = mean(dataMat, axis=0)
    meanRemoved = dataMat - meanVals #减去均值
    stded = meanRemoved / std(dataMat) #用标准差归一化
    covMat = cov(stded, rowvar=0) #求协方差方阵
    eigVals, eigVects = linalg.eig(mat(covMat)) #求特征值和特征向量
    eigValInd = argsort(eigVals)  #对特征值进行排序
    eigValInd = eigValInd[:-(topNfeat + 1):-1]
    redEigVects = eigVects[:, eigValInd]       # 除去不需要的特征向量
    lowDDataMat = stded * redEigVects    #求新的数据矩阵
    reconMat = (lowDDataMat * redEigVects.T) * std(dataMat) + meanVals
    return lowDDataMat, reconMat



if __name__ == '__main__':
    file_test="F:/guangpu.txt"
    data=loaddata(file_test)

    # meanVals=mean(data,axis=0)
    # meanRemoved=data-meanVals
    # covMat=cov(meanRemoved,rowvar=0)
    # eigVals,eigVects=linalg.eig(mat(covMat))
    # num=0
    # temp=0
    # for i in eigVals:
    #     temp=temp+i
    #     print(num,i,temp)
    #     num=num+1
    # print(eigVals[0]+eigVals[1]+eigVals[2]+eigVals[3])

    x,y = pca2(data,topNfeat=5)
    x,y = pca(data)
    # result=y[:,0:3]
    print(x.shape)
    print(y.shape)
    # print(result.shape)
    # print(result)
    # print(x)

    pass





















