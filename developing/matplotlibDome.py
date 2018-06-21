import matplotlib.pyplot as plt
import numpy as np
import pylab

def sanjiao():
   plt.plot([1, 2, 3])
   plt.ylabel('some numers')
   plt.show()
def imshowDome():
    points = np.arange(-5, 5, 0.01)
    xs, ys = np.meshgrid(points, points)
    print(xs)
    print(ys)
    z=np.sqrt(xs**2+ys**2)
    print(z)
    plt.imshow(z,cmap=plt.cm.gray)
    plt.colorbar()
    plt.title("Image plot of $\sqrt(x^2+y^2)$ for q grid fo values")
    pylab.show()

if __name__=='__main__':
   # sanjiao()
   #imshowDome()


