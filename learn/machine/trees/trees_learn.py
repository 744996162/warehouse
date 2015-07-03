#coding=utf-8
__author__ = 'Administrator'

from math import log
import operator


def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCount = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCount.keys():
            labelCount[currentLabel] = 0
        labelCount[currentLabel] += 1
    shannonEnt = 0.0

    for key in labelCount:
        prob = float(labelCount[key])/numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt

def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def choseBestFeatureToSplit(dataSet):
    numFatures = len(dataSet[0]) - 1
    baseEntorpy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1

    #遍历数据集中的每种特征
    for i in range(numFatures):
        featList = [ example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            #计算每种划分方式的信息
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntorpy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i

        return bestFeature


#多数表决
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
            classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

#创建决策树
#dataSet为数据集
#labels 为数据集的标签(实际含义)，算法中并不适用



def createTree(dataSet, labels):

    classList = [example[-1] for example in dataSet]

    #类别完全相同则停止继续划分
    if classList.count(classList[0]) == len(classList):
        return classList[0]

    #遍历完所有特征时返回出现次数最多的
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)

    bestFeat = choseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    fea

    pass


