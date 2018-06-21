from matplotlib import pylab
import numpy as np
def pylabDome():
    # 兼容 MATLAB 代码风格 API
    x = np.linspace(0, 10, 20)
    y = x * x + 2
    pylab.plot(x, y, 'r')
    pylab.show()
    # 绘制子图
    pylab.subplot(1, 2, 1)
    pylab.plot(x, y, 'r--')
    pylab.subplot(1, 2, 2)
    pylab.plot(y, x, 'g*-')
    pylab.show()

