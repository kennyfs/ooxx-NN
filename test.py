import numpy as np
a=np.mat(([1,1,4],[1,1,1]))
b=np.ones([3,2])
def plusmat(a,b):
	m1,n1=np.shape(a)
	m2,n2=np.shape(b)
	if m1!=m2:
		print 'different rows error'
		return
	returnmat=np.zeros([m1,n1+n2])
	returnmat[:,0:n1]=a[:,0:n1]
	returnmat[:,n1:(n1+n2)]=b[:,0:n2]
	return returnmat
print a*b
