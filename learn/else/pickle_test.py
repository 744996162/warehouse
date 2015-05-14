__author__ = 'zhangchao'
import pickle
# D={"a":1,"b":2}
# F=open('datafile.pk1','wb')
# pickle.dump(D,F)

F=open('datafile.pk1','rb')
E=pickle.load(F)
print(E)

