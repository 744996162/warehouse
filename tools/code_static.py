#coding=utf-8
__author__ = 'Administrator'
def LineTypePy(line, info):
    '''
    根据py的语法规则，分析此行代码属性，使代码还是注释。
    line：此行数据，info附加信息，在此无意义
    返回值：1代码，2注释，3代码和注释，0空行
    '''
    state, size = 0, len(line)
    line = line + '\n'
    i = -1 # 从0开始
    while i < size:
        i += 1
        if line[i] == '\n':     # 换行符
            break
        elif line[i] == ' ' or line[i] == '\t': # 空字符
            continue
        elif line[i] == '#' or line[i] == ';': # 注释起始符
            state |= 2
        else:
            state |= 1

    return state

def LineTypeC(line, info):
    '''
    根据C++的语法规则，分析此行代码属性，使代码还是注释。
    line：此行数据，info附加信息，是否是块注释
    返回值：1代码，2注释，3代码和注释，0空行
    '''
    state, size = 0, len(line)
    line = line + '\n' #添加一个字符防止越界
    i = -1
    while i < size:
        i += 1
        if line[i] == '\n':      # 换行符
            break
        elif line[i] == ' ' or line[i] == '\t': # 空字符
            continue
        elif line[i] == '/' and line[i+1] == '/':# 行注释
            state |= 2
            i += 1
        elif line[i] == '/' and line[i+1] == '*':# 块注释开始符
            state |= 2
            info[0] = 1
            i += 1
        elif line[i] == '*' and line[i+1] == '/':# 块注释结束符
            state |= 2
            info[0] = 0
            i += 1
        else:
            if info[0] == 0:
                state |= 1
            else:
                state |= 2
    return state

def CounteFile(res, typefunc, filename):
    '''
    统计文件
    res统计结果，typefunc行属性判断函数，filename文件名
    '''
    ret = [0,0,0,0,0]
    info = [0]
    for line in open(filename, 'rt'):
        ret[typefunc(line, info)] += 1
        ret[4] += 1 # 代码总行数
    res.append([filename,ret])

def CounteDir(res, typefunc, spath, modes, level):
    '''
    统计目录下的文件
    res统计结果，typefunc行属性判断函数，spath路径名
    modes文件后缀名，level统计几层子目录，-1为所有子目录
    '''
    import os
    import os.path
    eles = os.listdir(spath)
    dirs, files = [], []

    #区分文件和目录
    for ele in eles:
        ele = os.path.join(spath,ele)
        if os.path.isdir(ele):
            dirs.append(ele)
        else:
            files.append(ele)

    # 统计文件
    for f in files:
        isokfile = True
        if modes == []:
            pass
        else:
            for m in modes:
                if f[-len(m):] == m:
                    break
            else:
                isokfile = False
        if isokfile:
            CounteFile(res, typefunc, f)

    # 判断子目录是否计算完全
    if level == 0:
        return

    # 递归计算子目录
    for d in dirs:
        CounteDir(res, typefunc, d, modes, level-1)


class CodeCounter:
    '''
    代码统计器的类接口
    '''
    def __init__(self,codefiles=[],modes='.c,.h,.cpp',typefunc=LineTypeC,
                 codetype='c',level=1):
        self.level = level
        self.modes = modes
        self.codefiles = codefiles
        self.typefunc = typefunc
        self.codetype = codetype

    def Count(self, result):
        '''
        统计代码
        result为统计结果
        '''
        # 如果统计文件为空，默认统计当前目录
        if self.codefiles == []:
            self.codefiles.append(['d', '.'])

        for ele in self.codefiles:
            if ele[0] == 'f':   # 统计文件
                CounteFile(result, self.typefunc, ele[1])
            elif ele[0] == 'd': # 统计目录
                CounteDir(result, self.typefunc, ele[1],
                          self.modes.split(','), self.level)

    def SetCodeType(self, codetype):
        '''
        设置统计代码的类型
        codetype: py表示Python语言，c表示c或c++
        '''
        if codetype == 'py':
            self.typefunc = LineTypePy
        else:
            self.typefunc = LineTypeC
        self.codetype = codetype

    def AddCodeFiles(self, t, path):
        '''
        增加统计文件
        t表示文件类型,f表示文件，d表示目录
        path表示对应的文件或目录名字
        '''
        if t == 'f':
            self.codefiles.append(['f', path])
        elif t == 'd':
            self.codefiles.append(['d', path])

    def SetLevel(self, level):
        '''
        设置统计子目录的层次
        level表示统计几层子目录，0表示只统计当前目录，-1表示所有目录
        '''
        self.level = level

    def SetModes(self, modes):
        '''
        设置统计文件的后缀名
        modes 后缀名列表。例如[.c,.h]

'''
        self.modes = modes


if __name__ == '__main__':
    res = []
    counter = CodeCounter()
    counter.Count(res)

    stat = [0,0,0,0,0]
    for ele in res:
        print ele[1][4], ele[1][1]+ele[1][3], ele[1][2]+ele[1][3], ele[1][0], ele[0]
        for i in range(0, len(stat)):
            stat[i] += ele[1][i]

    print stat[4], stat[1]+stat[3], stat[2]+stat[3],stat[0],"Total"
