#!/usr/bin/python
D = {'a':'something','b':'someone'}
F = open('datafile.pkl','wb')

import pickle
pickle.dump(D, F)
F.close()
F = open('datafile.pkl','rb')
E = pickle.load(F)
print(E)
