
import csv
import numpy as np
import matplotlib.pyplot as plt
#READING CSV FILE
'''
f = open("ass-6.csv","r")
 
csv_f = csv.reader(f)
x = []
y = []
sig = []

for row in csv_f:
    x.append(float(row[0]))
    y.append(float(row[11]))
    sig.append(float(row[13]))'''

    
maty = np.loadtxt('ass-6.csv',delimiter= ',')

x = maty[:,0]

y = np.zeros(maty.shape[1] - 1)
temp = np.zeros((maty.shape[0],maty.shape[1] - 1))
stderr_t = np.zeros(maty.shape[1] - 1)
stderr_t2 = np.zeros(maty.shape[1] - 1)
w = np.zeros(maty.shape[1] - 1)

for i in range((maty.shape[1] - 1)):
    
    temp[i] = np.sum(maty[i,1:])/10
    y = np.power(temp,[2]*10)
    stderr_t[i] = np.sqrt(np.sum(np.power(temp[i] - maty[i,1:],[2]*10))/90)
    w[i] = (1/(stderr_t2[i])**2) 
print(temp)

print(y)
print(stderr_t)
print(w)    

n = len(x)
#Weights

'''
    
# parameter calculation    
Sw = sum(w)    
x_mean = 0
y_mean = 0
i = 0
while i < n :  
     x_mean += x[i]*w[i]/Sw
     y_mean += y[i]*w[i]/Sw
     i = i+1
        
Sxy = 0
Sy=0
Sxx =0
Syy = 0
Sx = 0
Sx2= 0
i = 0
while i < n:
        
      Sxy += w[i]*x[i]*y[i]
      Sy  += w[i]*y[i]
      Sxx += w[i]*(x[i]- x_mean)**2
      Syy += w[i]*(y[i] - y_mean)**2
      Sx += w[i]*x[i]
      Sx2 += w[i]*(x[i])**2
      i = i+1
      
N = (Sw*Sxy) - (Sx*Sy)      
D = Sw*Sx2 - (Sx)**2    
a1 = N/D
a0 = y_mean - a1*x_mean
r = (a1*np.sqrt(Sxx))/(np.sqrt(Syy))


print('slope','=>',a1)
print('intercept','=>',a0 )
print('correlation coefficient','=>',r)

#DEFINING  CORRESPONDING BEST FITTED Y VALUE FOR X

Y =[]
for i in x :
    Y.append(a1*i + a0)
  

chi_2 = 0
i = 0
while i < n:
    chi_2 += w[i]*(y[i] - Y[i])**2
    i = i+1
      
stdev = np.sqrt((n*chi_2)/((n-2)*Sw)) 
er_a1 = np.sqrt(Sw/(D))  
er_a0 = np.sqrt(Sx2/D)

print('Error in slope','=>',er_a1 )
print('Error in intercept','=>',er_a0)
print('chi squared','=>',chi_2)
print('standard deviation of predicted Y ','=>',stdev)

'''

































