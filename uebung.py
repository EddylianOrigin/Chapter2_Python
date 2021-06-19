import numpy as np
import matplotlib.pyplot as plt
list_1=[1,3,7,0,4,3.3,6,8.6,4]

def e_function(list_1):
    l=[np.exp(i) for i in list_1]

    x=np.array([1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0])
    y=np.array(l)
    plt.plot(x,y, color="blue")
    plt.show()


e_function(list_1)


