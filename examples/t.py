#距离矩阵计算
# 给定m*n阶矩阵X，满足X=[x1,x2,......xn],这里第i列向量是m维向量，
#求n*n矩阵，使得Dij=||Xi-Xj||的平方
# 方法3：
    #减少dot调用次数
    # D=(X-X)t(X-X)=
    # G=numpy.dot(X.T,X)
    # Dij=Gii-2Gij+Gjj