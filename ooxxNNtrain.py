import numpy as np
class net():
	def __init__(self):
		self.eb=0.01
		self.maxtraintimes=1000
		self.eta=0.05
		self.mc=0.4
		self.nh=10
		self.nhl=20
		self.no=1
		self.errlist=[]
		self.datamat=[]
		self.winner=[]
		self.ndatanum=0
		self.ndatadim=0
		self.owb=0
		self.hwb=[]
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
		for i in range(self.nhl):
			if i==0:
				hw=2.0*(np.random.rand(self.nh,self.ndatadim)-0.5)
				hb=2.0*(np.random.rand(self.nh,1)-0.5)
			else:
				hw=2.0*(np.random.rand(self.nh,self.nh)-0.5)
				hb=2.0*(np.random.rand(self.nh,1)-0.5)
			self.hwb.append(np.mat(self.plusmat(np.mat(hw),np.mat(hb))))
	def inito(self):
		ow=2.0*(np.random.rand(self.no,self.nh)-0.5)
		ob=2.0*(np.random.rand(self.no,1)-0.5)
		self.owb=np.mat(self.plusmat(np.mat(ow),np.mat(ob)))
	def plusmat(self,a,b,c=0):
		m1,n1=np.shape(a)
		m2,n2=np.shape(b)
		if m1!=m2:
			print('different rows error',m1,'!=',m2)
			return
		returnmat=np.zeros([m1,n1+n2])
		returnmat[:,0:n1]=a[:,0:n1]
		returnmat[:,(n1):(n1+n2)]=b[:,0:n2]
		if c:print('heeere',returnmat)
		return returnmat
	def bftrain(self):
		self.inith();self.inito()
		data=self.datamat.T
		winner=np.mat(self.winner)
		dowbOld=0.0
		dhwbOld=[]
		for i in range(self.nhl):
			dhwbOld.append([])
		i=0
		while(i<10000):
			self.eta=0.9-(i+1.0)*(0.9-0.05)/10000
			h_output=[]
			tonext=[]
			for j in range(self.nhl):
				if j==0:
					h_output.append(self.sigmoid(self.hwb[0]*data));
					tonext.append(self.plusmat(h_output[0].T,np.ones([self.ndatanum,1])).T)
				else:
					h_output.append(self.sigmoid(self.hwb[j]*tonext[j-1]));
					tonext.append(self.plusmat(h_output[j].T,np.ones([self.ndatanum,1])).T)
			o_output=self.sigmoid(self.owb*tonext[-1])
			err=winner-o_output
			sse=self.errorfunc(err)
			self.errlist.append(sse)
			o_delta=np.multiply(err,self.dlogit(o_output))
			h_delta=[]
			dhwb=[]
			for j in range(self.nhl):
				h_delta.append([]);dhwb.append([])
			j=self.nhl-1
			while j>=0:
				if j==self.nhl-1:
					h_delta[j]=np.multiply(self.owb[:,:-1].T*o_delta,self.dlogit(h_output[-1]))
				else:
					h_delta[j]=np.multiply(self.hwb[j+1][:,:-1].T*h_delta[j+1],self.dlogit(h_output[j]))
				if j==0:
					dhwb[0]=h_delta[0]*data.T
				else:
					dhwb[j]=h_delta[j]*tonext[j-1].T
				j-=1
			dowb=o_delta*tonext[-1].T
			if i==0:
				self.owb=self.owb+self.eta*dowb
				for j in range(self.nhl):
					self.hwb[j]=self.hwb[j]+self.eta*dhwb[j]
			else:
				self.owb=self.owb+(1.0-self.mc)*self.eta*dowb+self.mc*dowbOld
				for j in range(self.nhl):
					self.hwb[j]=self.hwb[j]+(1.0-self.mc)*self.eta*dhwb[j]+self.mc*dhwbOld[j]
			dowbOld=dowb;
			for j in range(self.nhl):
				dhwbOld[j]=dhwb[j]
			i+=1
			print('i:',i,'err:',sse,'eta:',self.eta)
a=net()
a.loaddata()
a.bftrain()
