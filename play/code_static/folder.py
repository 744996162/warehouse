#coding=utf-8
__author__ = 'Administrator'

class Folder:

    folder_name=None
    folder_path=None

    #初始化
    #传入文件夹路径，初始化文件夹路径，文件夹名
    def __init__(self,folder_path):
        self.folder_path=folder_path

    #返回该文件夹的文件名，str类型
    def getFolderName(self):
        pass


    #返回该文件夹的文件路径,str类型
    def getFolderPath(self):
        return self.folder_path
        pass


    #返回文件夹所在路径,str类型
    def getPath(self):
        pass

    #返回该文件夹下所有文件路径，list[str]类型
    def getAllFilePath(self):
        pass

    #返回该文件夹下所有文件的名字，list[str]类型
    def getAllFileName(self):
        pass


    #返回该文件夹下所有文件夹路径，list[str]类型
    def getAllFolderPath(self):
        pass

    #返回该文件夹下所有文件夹的名字，list[str]类型
    def getAllFolderName(self):
        pass

    #返回该文件夹下所有文件和文件夹的路径
    def getAllPath(self):
        pass

    #返回该文件夹下所有文件对象
    def getFile(self):
        pass

    #返回该文件夹下所有文件夹对象
    def getFolder(self):
        pass



