import numpy as np
a=np.ones([86,6])
b=np.zeros([86,1])
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
print np.shape(plusmat(a,b)),plusmat(a,b).T
