#coding=utf-8
from math import log
import operator
#计算给定数据集的香农熵

def calcShannonEnt(dataSet):
    numEntries=len(dataSet)
    labelCounts={}
    #为所有可能分类创建字典
    for featVec in dataSet:
        currentLabel=featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1
    shannonEnt=0.0

    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries
        #求对数
        shannonEnt-=prob*log(prob,2)
    return shannonEnt

#按照给定特征划分数据集
def splitDataSet(dataSet,axis,value):
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:
            reducedFeatVec=featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def choseBestFeatureToSplit(dataSet):
    numFeatures=len(dataSet[0])-1
    baseEntorpy=calcShannonEnt(dataSet)
    bestInfoGain=0.0
    bestFeature=-1
    #遍历数据集中的每种特征
    for i in range(numFeatures):
        featList=[example[i] for example in dataSet]
        uniqueVals=set(featList)
        newEntropy=0.0
        for value in uniqueVals:
            #计算每种划分方式的信息熵
            subDataSet=splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy+=prob*calcShannonEnt(subDataSet)
        infoGain=baseEntorpy-newEntropy
        if (infoGain>bestInfoGain):
            bestInfoGain=infoGain
            bestFeature=i
        return bestFeature

#多数表决
def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
            classCount[vote] += 1
    sortedClassCount=sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]



#创建决策树
##dataSet为数据集
##labels为数据集的标签(实际含义)，算法中并不使用

def createTree(dataSet,labels):
    classList=[example[-1] for example in dataSet]

    #类别完全相同则停止继续划分
    if classList.count(classList[0]) == len(classList):
        return classList[0]

    #遍历完所有特征时返回出现次数最多的
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)


    bestFeat=choseBestFeatureToSplit(dataSet)
    bestFeatLabeL=labels[bestFeat]
    myTree={bestFeatLabeL:{}}
    del(labels[bestFeat])
    featValues=[example[bestFeat] for example in dataSet]
    uniqueValues=set(featValues)
    for value in uniqueValues:
        subLabels=labels[:]
        myTree[bestFeatLabeL][value]=createTree(splitDataSet(dataSet,bestFeat,value),subLabels)

    return myTree




if  __name__== '__main__':

    pass

