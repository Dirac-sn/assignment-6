
import csv
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('bmh')
#READING CSV FILE
'''
f = open("trans.csv","r")
 
csv_f = csv.reader(f)
x = []
y = []

for row in csv_f:
    x.append(float(row[5]))
    y.append(float(row[6]))
'''
    
maty = np.loadtxt('ass-6.csv',delimiter= ',')

x = maty[:,0]

y = np.zeros(maty.shape[1] - 1)    
temp = np.zeros(maty.shape[1] - 1)

for i in range((maty.shape[1] - 1)):
    
    temp[i] = np.sum(maty[i,1:])/10
    y = np.power(temp,[2]*10)

print(temp)

#FINDING ESTIMATORS FOR REGRESSION
    
n = len(x) 
x_mean = sum(x)/n
y_mean = sum(y)/n
    
Sxy = 0
Sxx =0
Syy = 0
    
i = 0
while i < n:
        
      Sxy += (x[i] - x_mean)*(y[i] - y_mean)
      Sxx += (x[i]- x_mean)**2
      Syy += (y[i] - y_mean)**2
        
      i = i+1
       
a1 = Sxy/Sxx
a0 = y_mean - a1*x_mean
r = Sxy/np.sqrt(Sxx*Syy)
    
print('slope','=>',a1)
print('intercept','=>',a0 )
print('correlation coefficient','=>',r)

#DEFINING  CORRESPONDING BEST FITTED Y VALUE FOR X

Y =[]
for i in x :
    Y.append(a1*i + a0)
  
    
print('Estimated Y','==>')
print(Y)

#SUM OF RESUDIALS AND SQUARED RESIDUALS
SR = 0
SSR = 0
i = 0
while i < n:
    
    SR += y[i] - Y[i]
    SSR+= (y[i] - Y[i])**2
    i = i+1
    
print('Sum of Residuals','=>',SR)
print('Sum of squared Residuals','=>',SSR)


#STANDARD ERROR IN ESTIMATORS OF SLOPE AND INTECEPT

Var_est = (SSR/(n-2))

#IT IS A VARIANCE ESTIMATOR FOR SAMPLE NORMAL DISTRIBUTION AROUND SLOPE ESTIMATOR

s = np.sqrt(Var_est)

err_slope = s/np.sqrt(Sxx)
err_inter = s*np.sqrt((1/n)+((x_mean)**2/Sxx))
print('Standard error in slope','=>',err_slope)
print('Standard error in intercept','=>',err_inter)


#PLOTTING LEAST SQUARE FIT GRAPH    

plt.scatter(x,y, c = 'magenta',s= 70 ,edgecolors='black',alpha=0.95)
plt.plot(x,Y, 'r' , linewidth = 1.5)
plt.show 


plt.title('least Square fitted line - For Transverse Standing Wave')
plt.xlabel(' T - Tension in the String ')
plt.ylabel(' Wavelength Squared - Y variable ')

 
    
    



