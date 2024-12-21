import pickle
l=[3,4,5,3]

write=open('writefile.txt','wb')

pickle.dump(l,write)

write.close()