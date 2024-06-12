#GRAPHS IN PYTHON
import matplotlib.pyplot as plt
#Matplotlib: useful for making graphs in python

x= [1,2,3,4,5]
y= [1,4,9,16,25] #y=x^2

#linear graph
#plt.plot(x,y)
#plt.show()

#scatterplot
plt.plot(x,y, "ro") #R sets color to red, the o makes it a sctterplot
#colors: [r,b,y,g]
#line types [ o, -, *, 1, 2, 3, 4, .]
plt.show()
