import numpy as np
class net():
	def __init__(self):
		self.eb=0.01
		self.maxtraintimes=1000
		self.eta=0.05
		self.mc=0.2
		self.maxtimestrain=100
		self.nh=6
		self.no=1
		self.errlist=[]
		self.datamat=[]
		self.winner=[]
		self.ndatanum=0
		self.ndatadim=0
	def loaddata(self):
		self.datamat=[];self.winner=[]
		f=open('ooxxdata.txt')
		gamelen=0
		for line in f.readlines():
			linearr=line.strip().split()
			linearr=[float(i) for i in linearr]
			if(len(linearr)==18):
				gamelen+=1
				linearr.append(1.0)
				self.datamat.append(linearr)
			else:
				for j in range(gamelen):
					self.winner.append(linearr[0])
				gamelen=0
		self.datamat=np.mat(self.datamat)
		m,n=np.shape(self.datamat)
		self.ndatanum=m
		self.ndatadim=n-1
	def dlogit(self,amat):
		return np.multiply(amat,(1.0-amat))
	def errorfunc(self,x):
		return np.sum(np.power(x,2))
	def sigmoid(self,amat):
		return 1.0/(1.0+np.exp(-amat))
	def inith(self):
		hw=2.0*(np.random.rand(self.nh,self.ndatadim)-0.5)
		hb=2.0*(np.random.rand(self.nh,1)-0.5)
		self.hwb=np.mat(self.plusmat(np.mat(hw),np.mat(hb)))
	def inito(self):
		ow=2.0*(np.random.rand(self.no,self.nh)-0.5)
		ob=2.0*(np.random.rand(self.no,1)-0.5)
		self.owb=np.mat(self.plusmat(np.mat(ow),np.mat(ob)))
	def plusmat(self,a,b):
		m1,n1=np.shape(a)
		m2,n2=np.shape(b)
		if m1!=m2:
			print 'different rows error'
			return
		returnmat=np.zeros([m1,n1+n2])
		returnmat[:,0:n1]=a[:,0:n1]
		returnmat[:,n1:(n1+n2)]=b[:,0:n2]
		return returnmat
	def bftrain(self):
		self.inith();self.inito()
		data=self.datamat.T
		winner=np.mat(self.winner)
		dowbOld=0.0;dhwbOld=0.0
		i=0
		while(i<100000):
			self.eta=0.2-(i+1.0)*(0.2-0.05)/100000
			h_output=self.sigmoid(self.hwb*data)
			h2o=self.plusmat(h_output.T,np.ones((self.ndatanum,1))).T
			o_output=self.sigmoid(self.owb*h2o)
			err=winner-o_output
			sse=self.errorfunc(err)
			self.errlist.append(sse)
			o_delta=np.multiply(err,self.dlogit(o_output))
			h_delta=np.multiply(self.owb[:,:-1].T*o_delta,self.dlogit(h_output))
			dowb=o_delta*h2o.T
			dhwb=h_delta*data.T
			if i==0:
				self.owb=self.owb+self.eta*dowb
				self.hwb=self.hwb+self.eta*dhwb
			else:
				self.owb=self.owb+(1.0-self.mc)*self.eta*dowb+self.mc*dowbOld
				self.hwb=self.hwb+(1.0-self.mc)*self.eta*dhwb+self.mc*dhwbOld
			dowbOld=dowb;dhwbOld=dhwb
			i+=1
			print 'i:',i,'err:',sse,'eta:',self.eta
a=net()
a.loaddata()
a.bftrain()
			
