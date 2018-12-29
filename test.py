import numpy as np
a=np.zeros([2,2])
print a
a[:,0:1]=x=np.mat(np.ones([2,1]))+5
a[:,1:2]=y=np.mat(np.ones([2,1]))
print 'a:',a
print 'x:',x
print 'y:',y
